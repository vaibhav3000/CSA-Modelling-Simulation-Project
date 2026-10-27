# =============================================================================
# E0240 Project - Phase 2 GPU sweep for Phi-3-mini (paste into ONE Colab cell,
# or upload as a file and run:  !python colab_sweep.py)
#
# What it does: for each (model, workload, batch size B, trial) it runs ONE
# static batched generation call on the GPU, UNCAPPED (max_new_tokens=512),
# greedy decoding, and logs wall time + the generated length of every sequence.
# Results are appended to a CSV after EVERY batch, and finished rows are
# skipped on re-run, so a Colab disconnect never loses work.
# =============================================================================
import os, sys, json, time, random, subprocess, csv

subprocess.run([sys.executable, "-m", "pip", "install", "-q",
                "transformers", "accelerate", "datasets"], check=False)

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# ----------------------------- SETTINGS --------------------------------------
MODELS = ["microsoft/Phi-3-mini-4k-instruct"]
TAG = "phi3"                      # used in the output file name
BATCH_SIZES   = [1, 2, 4, 8, 16, 32]
TRIALS        = 5          # trials per (model, workload, B). Lower to 3 if short on time.
MAX_NEW       = 512        # UNCAPPED regime (the old 96 cap was the problem)
POOL_SIZE     = 100        # prompts per workload
MAX_PROMPT_TOK = 600       # truncate long prompts to this many tokens
SEED          = 20261023
OUT_DIR       = "/content/sweep_out"          # local Colab disk
USE_DRIVE     = True                          # also copy results to Google Drive
# TIP: run  drive.mount('/content/drive')  in a SEPARATE cell BEFORE this script.
# Optional: upload your old prompts.json (100 short factual questions) to
# /content/prompts.json to reuse it for the short-QA workload.
# ------------------------------------------------------------------------------

os.makedirs(OUT_DIR, exist_ok=True)
if USE_DRIVE:
    try:
        from google.colab import drive
        drive.mount("/content/drive")
        DRIVE_DIR = "/content/drive/MyDrive/e0240_sweep_out"
        os.makedirs(DRIVE_DIR, exist_ok=True)
    except Exception as e:
        print("Drive not mounted (continuing without):", e)
        DRIVE_DIR = None
else:
    DRIVE_DIR = None

assert torch.cuda.is_available(), "No GPU! Runtime > Change runtime type > T4 GPU"
print("GPU:", torch.cuda.get_device_name(0), "| torch", torch.__version__)

# ------------------------------ WORKLOADS ------------------------------------
def load_workloads():
    W = {}
    # 1) short factual Q&A
    if os.path.exists("/content/prompts.json"):
        qa = json.load(open("/content/prompts.json"))
        qa = [q if isinstance(q, str) else q.get("prompt", str(q)) for q in qa]
    else:
        topics = ["photosynthesis", "the French Revolution", "black holes", "inflation",
                  "the water cycle", "vaccines", "plate tectonics", "the internet",
                  "machine learning", "the Roman Empire"]
        qa = [f"Explain {t} clearly." for t in topics] * 10
    W["short_qa"] = qa[:POOL_SIZE]

    from datasets import load_dataset
    # 2) long-prompt summarization
    try:
        ds = load_dataset("abisee/cnn_dailymail", "3.0.0", split=f"test[:{POOL_SIZE}]")
        W["summarize"] = ["Summarize the following article in a few sentences:\n\n" + a
                          for a in ds["article"]]
    except Exception as e:
        print("!! summarization dataset failed to load:", e)
    # 3) code generation
    try:
        ds = load_dataset("openai/openai_humaneval", split="test")
        W["code"] = ["Complete this Python function and explain it briefly:\n\n" + p
                     for p in ds["prompt"]][:POOL_SIZE]
    except Exception as e:
        print("!! code dataset failed to load:", e)
    return W

WORKLOADS = load_workloads()
print({k: len(v) for k, v in WORKLOADS.items()})

# ------------------------------- HELPERS -------------------------------------
CSV_PATH = os.path.join(OUT_DIR, f"sweep_{TAG}.csv")
FIELDS = ["model", "workload", "B", "trial", "wall_time_s", "max_prompt_tokens",
          "max_len", "mean_len", "min_len", "total_tokens", "n_hit_cap",
          "peak_mem_gb", "lengths_json", "do_sample", "status"]

def done_keys():
    if not os.path.exists(CSV_PATH):
        return set()
    with open(CSV_PATH) as f:
        return {(r["model"], r["workload"], int(r["B"]), int(r["trial"]))
                for r in csv.DictReader(f) if r.get("status", "ok") == "ok"}

def append_row(row):
    new = not os.path.exists(CSV_PATH)
    with open(CSV_PATH, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        if new:
            w.writeheader()
        w.writerow(row)
    if DRIVE_DIR:
        try:
            import shutil; shutil.copy(CSV_PATH, os.path.join(DRIVE_DIR, f"sweep_{TAG}.csv"))
        except Exception:
            pass

def build_prompt(tok, text):
    msgs = [{"role": "user", "content": text}]
    return tok.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True)

def truncate_text(tok, text, max_tok):
    ids = tok(text, add_special_tokens=False)["input_ids"]
    if len(ids) > max_tok:
        text = tok.decode(ids[:max_tok])
    return text

def seq_lengths(gen_ids, eos_ids, pad_id):
    """number of generated tokens per row, counting through the first EOS."""
    lens = []
    for row in gen_ids.tolist():
        n = len(row)
        for i, t in enumerate(row):
            if t in eos_ids:
                n = i + 1
                break
        lens.append(n)
    return lens

# -------------------------------- MAIN ---------------------------------------
finished = done_keys()
for model_name in MODELS:
    print("\n=== Loading", model_name)
    tok = AutoTokenizer.from_pretrained(model_name)
    tok.padding_side = "left"
    if tok.pad_token is None:
        tok.pad_token = tok.eos_token
    model = AutoModelForCausalLM.from_pretrained(
        model_name, torch_dtype=torch.float16, device_map="cuda")
    model.eval()
    cfg = model.config
    kv_heads = getattr(cfg, "num_key_value_heads", cfg.num_attention_heads)
    head_dim = cfg.hidden_size // cfg.num_attention_heads
    kv_bytes_tok = 2 * cfg.num_hidden_layers * kv_heads * head_dim * 2   # K+V, fp16
    n_params = sum(p.numel() for p in model.parameters())
    print(f"CONFIG layers={cfg.num_hidden_layers} hidden={cfg.hidden_size} "
          f"heads={cfg.num_attention_heads} kv_heads={kv_heads} "
          f"params={n_params/1e9:.2f}B  KV cache/token={kv_bytes_tok/1024:.0f} KiB "
          f"weights={torch.cuda.memory_allocated()/1e9:.2f} GB")
    oom_at = {}
    eos = model.generation_config.eos_token_id
    eos_ids = set(eos if isinstance(eos, list) else [eos if eos is not None else tok.eos_token_id])

    # warm-up (not recorded)
    w = tok([build_prompt(tok, "Hello")], return_tensors="pt", padding=True).to("cuda")
    with torch.no_grad():
        model.generate(**w, max_new_tokens=8, do_sample=False)
    torch.cuda.synchronize()

    for wname, pool in WORKLOADS.items():
        texts = [truncate_text(tok, t, MAX_PROMPT_TOK) for t in pool]
        prompts = [build_prompt(tok, t) for t in texts]
        for B in BATCH_SIZES:
            if wname in oom_at and B >= oom_at[wname]:
                continue
            for trial in range(1, TRIALS + 1):
                key = (model_name, wname, B, trial)
                if key in finished:
                    continue
                rng = random.Random(f"{SEED}-{wname}-{B}-{trial}")
                idx = rng.sample(range(len(prompts)), min(B, len(prompts)))
                if B > len(prompts):               # pool smaller than B: sample with repeat
                    idx = [rng.randrange(len(prompts)) for _ in range(B)]
                batch = [prompts[i] for i in idx]
                enc = tok(batch, return_tensors="pt", padding=True).to("cuda")
                in_len = enc["input_ids"].shape[1]
                torch.cuda.empty_cache()
                torch.cuda.reset_peak_memory_stats()
                try:
                    torch.cuda.synchronize(); t0 = time.perf_counter()
                    with torch.no_grad():
                        out = model.generate(**enc, max_new_tokens=MAX_NEW,
                                             do_sample=False, temperature=None,
                                             top_p=None, top_k=None)
                    torch.cuda.synchronize(); dt = time.perf_counter() - t0
                except torch.cuda.OutOfMemoryError:
                    print(f"OOM at {model_name} {wname} B={B}; skipping this B and larger")
                    append_row(dict(model=model_name, workload=wname, B=B, trial=trial,
                                    wall_time_s="", max_prompt_tokens=in_len, max_len="",
                                    mean_len="", min_len="", total_tokens="", n_hit_cap="",
                                    peak_mem_gb=round(torch.cuda.max_memory_allocated()/1e9, 2),
                                    lengths_json="", do_sample=False, status="oom"))
                    oom_at[wname] = B
                    del enc
                    import gc; gc.collect(); torch.cuda.empty_cache()
                    break
                gen = out[:, in_len:]
                lens = seq_lengths(gen, eos_ids, tok.pad_token_id)
                row = dict(model=model_name, workload=wname, B=B, trial=trial,
                           wall_time_s=round(dt, 4), max_prompt_tokens=in_len,
                           max_len=max(lens), mean_len=round(sum(lens) / len(lens), 2),
                           min_len=min(lens), total_tokens=sum(lens),
                           n_hit_cap=sum(1 for L in lens if L >= MAX_NEW),
                           peak_mem_gb=round(torch.cuda.max_memory_allocated() / 1e9, 2),
                           lengths_json=json.dumps(lens), do_sample=False, status="ok")
                append_row(row)
                print(f"{model_name.split('/')[-1]:<22} {wname:<10} B={B:<2} t{trial} "
                      f"{dt:6.1f}s  maxlen={max(lens):<3} meanlen={row['mean_len']}")
    del model
    torch.cuda.empty_cache()

print("\nDONE. Results:", CSV_PATH)
if DRIVE_DIR:
    print("Copy also in Google Drive folder: e0240_sweep_out")
