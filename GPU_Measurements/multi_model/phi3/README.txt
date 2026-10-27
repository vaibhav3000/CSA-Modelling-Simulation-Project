Phi-3-mini-4k-instruct GPU sweep (Colab Tesla T4, fp16, static batching, greedy, max_new_tokens=512)
sweep_phi3.csv       - results: 75 ok rows + 2 OOM rows (status column). Workloads: short_qa, summarize, code.
colab_sweep_phi3.py  - the exact script that produced it.
Notes: OOM at summarize B=16 and code B=32 (Phi-3 KV cache ~384 KiB/token). Throughput gain only ~3x at B=16-32.
