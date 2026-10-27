 =============================================================================
# E0240 Phase 2 GPU sweep - Llama-3.2-1B-Instruct, FINAL single run
# Same protocol as the Phi-3 sweep: static batch, greedy, UNCAPPED (512 tokens),
# 3 workloads, B = 1..32, 5 trials. Results are appended to a CSV after every
# batch and finished rows are skipped on re-run, so a disconnect loses nothing.
#
# BEFORE RUNNING: Runtime > Change runtime type > T4 GPU, and add your Hugging
# Face token as a Colab secret named HF_TOKEN (key icon on the left, turn on
# "Notebook access").
# =============================================================================
import os, sys, json, time, random, subprocess, csv, gc, shutil

subprocess.run([sys.executable, "-m", "pip", "install", "-q",
                "transformers", "accelerate", "datasets"], check=False)

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from huggingface_hub import login

# ----------------------------- SETTINGS --------------------------------------
MODEL_NAME     = "meta-llama/Llama-3.2-1B-Instruct"
TAG            = "llama32_1b_final"   # output: sweep_llama32_1b_final.csv  (rename to sweep_llama32_1b.csv when sharing)
BATCH_SIZES    = [1, 2, 4, 8, 16, 32]
TRIALS         = 5
MAX_NEW        = 512               # uncapped regime (use 96 + a new TAG for a capped pass)
POOL_SIZE      = 100
MAX_PROMPT_TOK = 600
SEED           = 20261023          # same as the Phi-3 run -> same batches
ONLY_WORKLOADS = None              # None = all three; or e.g. ["short_qa"]
OUT_DIR        = "/content/sweep_out"
USE_DRIVE      = True              # also copy results to Google Drive
# Optional: upload your 100-question prompts.json to /content/prompts.json
# (use the same file your teammate used for the short_qa workload).
# ------------------------------------------------------------------------------

# --- Hugging Face login (Llama is gated) ---
try:
    from google.colab import userdata
    login(token=userdata.get("HF_TOKEN"))
except Exception as e:
    print("No HF_TOKEN secret found (", e, ") -> paste your token below")
    from huggingface_hub import notebook_login
    notebook_login()

os.makedirs(OUT_DIR, exist_ok=True)
DRIVE_DIR = None
if USE_DRIVE:
    try:
        from google.colab import drive
        drive.mount("/content/drive")
        DRIVE_DIR = "/content/drive/MyDrive/e0240_sweep_out"
        os.makedirs(DRIVE_DIR, exist_ok=True)
    except Exception as e:
        print("Drive not mounted (continuing without):", e)

assert torch.cuda.is_available(), "No GPU! Runtime > Change runtime type > T4 GPU"
GPU_NAME = torch.cuda.get_device_name(0)
print("GPU:", GPU_NAME, "| torch", torch.__version__)
if "T4" not in GPU_NAME:
    print("WARNING: not a T4 - timings will not be comparable with the other runs!")

# ------------------------------ WORKLOADS ------------------------------------
def load_workloads():
    W = {}
    if os.path.exists("/content/prompts.json"):
        qa = json.load(open("/content/prompts.json"))
        qa = [q if isinstance(q, str) else q.get("prompt", str(q)) for q in qa]
        W["short_qa"] = qa[:POOL_SIZE]
    else:
        raise FileNotFoundError("Upload prompts.json to /content/prompts.json first "
                                "(Colab left sidebar > Files > upload), then re-run.")

    from datasets import load_dataset
    try:
        ds = load_dataset("abisee/cnn_dailymail", "3.0.0", split=f"test[:{POOL_SIZE}]")
        W["summarize"] = ["Summarize the following article in a few sentences:\n\n" + a
                          for a in ds["article"]]
    except Exception as e:
        print("!! summarization dataset failed to load:", e)
    try:
        ds = load_dataset("openai/openai_humaneval", split="test")
        W["code"] = ["Complete this Python function and explain it briefly:\n\n" + p
                     for p in ds["prompt"]][:POOL_SIZE]
    except Exception as e:
        print("!! code dataset failed to load:", e)
    return W

WORKLOADS = load_workloads()
if ONLY_WORKLOADS:
    WORKLOADS = {k: v for k, v in WORKLOADS.items() if k in ONLY_WORKLOADS}
print("workloads to run:", {k: len(v) for k, v in WORKLOADS.items()})
assert WORKLOADS, "No workload to run (is prompts.json uploaded?)"

# ------------------------------- HELPERS -------------------------------------
CSV_PATH = os.path.join(OUT_DIR, f"sweep_{TAG}.csv")
FIELDS = ["model", "workload", "B", "trial", "wall_time_s", "max_prompt_tokens",
          "max_len", "mean_len", "min_len", "total_tokens", "n_hit_cap",
          "peak_mem_gb", "lengths_json", "do_sample", "status"]

def sync_to_drive(path):
    if DRIVE_DIR:
        try:
            shutil.copy(path, os.path.join(DRIVE_DIR, os.path.basename(path)))
        except Exception:
            pass

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
    sync_to_drive(CSV_PATH)

def build_prompt(tok, text):
    msgs = [{"role": "user", "content": text}]
    # the Llama template already contains <|begin_of_text|>
    return tok.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True)

def truncate_text(tok, text, max_tok):
    ids = tok(text, add_special_tokens=False)["input_ids"]
    return tok.decode(ids[:max_tok]) if len(ids) > max_tok else text

def seq_lengths(gen_ids, eos_ids):
    """generated tokens per row, counting through the first EOS."""
    lens = []
    for row in gen_ids.tolist():
        n = len(row)
        for i, t in enumerate(row):
            if t in eos_ids:
                n = i + 1
                break
        lens.append(n)
    return lens

# -------------------------------- MODEL --------------------------------------
print("\n=== Loading", MODEL_NAME)
tok = AutoTokenizer.from_pretrained(MODEL_NAME)
tok.padding_side = "left"
if tok.pad_token is None:
    tok.pad_token = tok.eos_token
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME, torch_dtype=torch.float16, device_map="cuda")
model.eval()

cfg = model.config
kv_heads = getattr(cfg, "num_key_value_heads", cfg.num_attention_heads)
head_dim = getattr(cfg, "head_dim", None) or cfg.hidden_size // cfg.num_attention_heads
kv_bytes_tok = 2 * cfg.num_hidden_layers * kv_heads * head_dim * 2     # K+V, fp16
n_params = sum(p.numel() for p in model.parameters())
weights_gb = torch.cuda.memory_allocated() / 1e9
info = dict(model=MODEL_NAME, gpu=GPU_NAME, layers=cfg.num_hidden_layers,
            hidden=cfg.hidden_size, heads=cfg.num_attention_heads, kv_heads=kv_heads,
            head_dim=head_dim, params_B=round(n_params / 1e9, 3),
            kv_bytes_per_token=kv_bytes_tok, kv_KiB_per_token=kv_bytes_tok / 1024,
            weights_gb=round(weights_gb, 3), max_new=MAX_NEW)
print("CONFIG", info)
cfg_path = os.path.join(OUT_DIR, f"config_{TAG}.json")
json.dump(info, open(cfg_path, "w"), indent=2)
sync_to_drive(cfg_path)

eos = model.generation_config.eos_token_id
eos_ids = set(eos if isinstance(eos, list) else [eos if eos is not None else tok.eos_token_id])

# Does the chat template already contain BOS? (Llama-3.2: yes, TinyLlama: no)
# If yes we must not add a second one; if no, the tokenizer has to add it.
_test = build_prompt(tok, "Hello")
ADD_SPECIAL = not (tok.bos_token is not None and _test.startswith(tok.bos_token))
print("template starts with BOS:", not ADD_SPECIAL, "-> add_special_tokens =", ADD_SPECIAL)

# warm-up (not recorded)
w = tok([_test], return_tensors="pt",
        padding=True, add_special_tokens=ADD_SPECIAL).to("cuda")
with torch.no_grad():
    model.generate(**w, max_new_tokens=8, do_sample=False,
                   temperature=None, top_p=None, top_k=None)
torch.cuda.synchronize()

# -------------------------------- SWEEP --------------------------------------
finished = done_keys()
oom_at = {}
for wname, pool in WORKLOADS.items():
    texts = [truncate_text(tok, t, MAX_PROMPT_TOK) for t in pool]
    prompts = [build_prompt(tok, t) for t in texts]
    for B in BATCH_SIZES:
        if wname in oom_at and B >= oom_at[wname]:
            continue
        for trial in range(1, TRIALS + 1):
            if (MODEL_NAME, wname, B, trial) in finished:
                continue
            rng = random.Random(f"{SEED}-{wname}-{B}-{trial}")
            idx = rng.sample(range(len(prompts)), min(B, len(prompts)))
            if B > len(prompts):
                idx = [rng.randrange(len(prompts)) for _ in range(B)]
            batch = [prompts[i] for i in idx]
            enc = tok(batch, return_tensors="pt", padding=True,
                      add_special_tokens=ADD_SPECIAL).to("cuda")   # never a double BOS
            in_len = enc["input_ids"].shape[1]
            torch.cuda.empty_cache()
            torch.cuda.reset_peak_memory_stats()
            try:
                torch.cuda.synchronize(); t0 = time.perf_counter()
                with torch.no_grad():
                    out = model.generate(**enc, max_new_tokens=MAX_NEW, do_sample=False,
                                         temperature=None, top_p=None, top_k=None)
                torch.cuda.synchronize(); dt = time.perf_counter() - t0
            except torch.cuda.OutOfMemoryError:
                print(f"OOM at {wname} B={B}; skipping this B and larger")
                append_row(dict(model=MODEL_NAME, workload=wname, B=B, trial=trial,
                                wall_time_s="", max_prompt_tokens=in_len, max_len="",
                                mean_len="", min_len="", total_tokens="", n_hit_cap="",
                                peak_mem_gb=round(torch.cuda.max_memory_allocated() / 1e9, 2),
                                lengths_json="", do_sample=False, status="oom"))
                oom_at[wname] = B
                del enc
                gc.collect(); torch.cuda.empty_cache()
                break
            lens = seq_lengths(out[:, in_len:], eos_ids)
            row = dict(model=MODEL_NAME, workload=wname, B=B, trial=trial,
                       wall_time_s=round(dt, 4), max_prompt_tokens=in_len,
                       max_len=max(lens), mean_len=round(sum(lens) / len(lens), 2),
                       min_len=min(lens), total_tokens=sum(lens),
                       n_hit_cap=sum(1 for L in lens if L >= MAX_NEW),
                       peak_mem_gb=round(torch.cuda.max_memory_allocated() / 1e9, 2),
                       lengths_json=json.dumps(lens), do_sample=False, status="ok")
            append_row(row)
            print(f"{wname:<10} B={B:<2} t{trial} {dt:6.1f}s  "
                  f"maxlen={max(lens):<3} meanlen={row['mean_len']}")

# ------------------------------- SUMMARY -------------------------------------
print("\nDONE. Results:", CSV_PATH)
print("\nSUMMARY  (ms/step = wall time / longest sequence)")
print(f"{'workload':<10} {'B':>3} {'n':>2} {'wall_s':>8} {'max_len':>8} {'ms/step':>8}")
rows = [r for r in csv.DictReader(open(CSV_PATH)) if r["status"] == "ok"]
for wname in WORKLOADS:
    for B in BATCH_SIZES:
        rs = [r for r in rows if r["workload"] == wname and int(r["B"]) == B]
        if not rs:
            continue
        wall = sum(float(r["wall_time_s"]) for r in rs) / len(rs)
        ml = sum(int(r["max_len"]) for r in rs) / len(rs)
        ms = sum(float(r["wall_time_s"]) / int(r["max_len"]) * 1000 for r in rs) / len(rs)
        print(f"{wname:<10} {B:>3} {len(rs):>2} {wall:>8.1f} {ml:>8.0f} {ms:>8.1f}")
print("\nSave these 2 files:", CSV_PATH, "and", cfg_path)