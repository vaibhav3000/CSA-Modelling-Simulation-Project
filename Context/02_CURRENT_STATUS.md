# 02 — Current Project Status

## 1. What Is Completed & Verified

### A. Core Simulator Engine (`Project_Simulator/`)
- **Discrete-Event Simulation Loop:** Fully implemented in `network_sim.py` using cycle-driven discrete-event simulation with inverse transform random variate generation (uniform seed `20260922`).
- **Station Implementations:**
  - $Q_1$: Deterministic tokenizer server ($Geo/D/1$, $S_1 = 2$).
  - $Q_2$: Dual-trigger FCFS batch buffer (batch cap $B$, timer threshold $\tau$).
  - $Q_3$: Multi-worker parallel decode engine ($Geo/Geo/c$ baseline with parameter $p_s = 1 / E[S_3]$).
- **Accounting Verification:** Verified flow conservation ($\lambda_1 = \lambda_2 = \lambda_3$), Little's Law ($W = L_q / \lambda$), and theoretical server utilization ($\rho_i = \lambda E[S_i]$) with discrepancy $\le 3.4 \times 10^{-7}$.

### B. Analytical Validation Suite (Layer 1)
- **Closed-Form Verification:**
  - $Geo/D/1$ ($S = 2$): Verified simulated $L_q$ against $L_q = \lambda^2 / (1 - 2\lambda)$ across $\lambda \in [0.05, 0.45]$ over $10^7$ cycles; error $< 0.75\%$.
  - $Geo/Geo/1$ ($E[S] = 2$): Verified simulated $L_q$ against $L_q = 2\lambda^2 / (1 - 2\lambda)$; confirmed exact factor-of-2 variance penalty within $0.94\%$ relative error.
  - Convergence check: Verified convergence of time-average queue length from $10^3$ to $10^7$ cycles.
- **Run Artifacts:** Result CSVs (`validation_table.csv`, `validation_factor2.csv`, `validation_geo_d_1_S2.csv`, etc.) and vector plots in `Project_Simulator/figures/`.

### C. Simulation Experiments (E2 & E3)
- **Experiment E2 (Pipeline & Worker Scaling):**
  - Swept injection rate $\lambda \in [0.05, 0.45]$ across worker pools $c \in \{1, 2\}$.
  - Characterized per-station delay breakdown and end-to-end latency scaling.
  - Output CSV: `Project_Simulator/results/experiment_e2_pipeline.csv`.
- **Experiment E3 (Batching Trade-Off Sweep):**
  - Mapped 2D parameter space of batch capacity $B \in \{1, 4, 8, 16, 32\}$ and timeout threshold $\tau \in \{1, 2, 5, 10\}$ at fixed injection loads.
  - Captured the throughput vs. latency trade-off curve (small $B$ minimizes queue delay; large $B$ maximizes worker utilization).
  - Output CSV: `Project_Simulator/results/experiment_e3_batching.csv`.

### D. Empirical GPU Measurement Campaign (Layer 2)
- **Hardware Target:** Nvidia Tesla T4 GPU (Google Colab & Kaggle, CUDA 12.8, PyTorch).
- **Workload:** `Qwen/Qwen2.5-1.5B-Instruct`, fp16, CUDA-synchronized wall-clock timing.
- **Batching Sweep:** 6 batch sizes $B \in \{1, 2, 4, 8, 16, 32\}$ with 10 trials per size.
- **Split Calibration & Held-Out Prediction:**
  - Calibration set: $B \in \{1, 4, 16\}$ fitted to power law $T = a \cdot B^\alpha$ ($a \approx 4.0301$, $\alpha \approx 0.00104$).
  - Held-out test set: $B \in \{2, 8, 32\}$ predicted with **4.43% MAPE** on batch execution latency and **4.18% MAPE** on throughput.
- **Response-Length vs. Linear Predictor:**
  - Max-sequence-length predictor achieved **9.14% MAPE** vs. **15.25% MAPE** for simple linear-in-$B$ scaling (`NAME3_GPU_Analysis/name3_summary.csv`).
- **Uncapped Length Diagnostic:**
  - 100 prompts measured with 512 token cap (0/100 capped).
  - Empirical distribution demonstrated geometric Kolmogorov-Smirnov distance $KS = 0.3965$, revealing that real LLM decode length is heavy-tailed and not purely memoryless geometric.
- **Tokenizer Overhead:** 20 trials collected, mean latency $0.206\text{ ms}$, max $1.37\text{ ms}$.

---

## 2. What Is Still Pending for Phase 2

1. **Formal Cycle-to-Millisecond Mapping (`cycle_ms`):**
   - In `calibration_parameters.json`, `"cycle_ms"` is currently `null`.
   - Need to establish the exact physical conversion factor (e.g. 1 cycle = $10\text{ ms}$ or $20\text{ ms}$) so empirical batch time directly determines the cycle duration of $Q_3$ decode jobs.
2. **Strengthen Pipeline Motivation in Report (Phase 2 Section I & III):**
   - Address Professor Feedback #1 by explicitly diagramming the physical serving architecture (vLLM / TGI) and showing how TTFT and ITL are decomposed across $Q_1$, $Q_2$, and $Q_3$.
3. **Expand Empirical Rigor & Diversity (Phase 2 Section IV & V):**
   - Address Professor Feedback #2 by comparing model scaling (e.g. Qwen 0.5B vs 1.5B vs larger architectures) and discussing query length distribution impacts (e.g. conversational vs long context).
   - Reconcile the capped sweep (4.43% MAPE) with the uncapped diagnostic (9.14% MAPE) and present both transparently.
4. **Draft and Typeset the 4-Page IEEE Phase 2 Report:**
   - **Completed:** Written and compiled `phase2_report.tex` and `phase2_report.pdf` (exactly 4 pages in IEEE conference format) meeting all course requirements and addressing professor feedback.
   - Target deadline: **27 October 2026**.

---

## 3. Location of Key Files

| Category | Primary Directory / Path | Notes |
|---|---|---|
| **Simulator Engine** | `Project_Simulator/network_sim.py` | Discrete-event 3-station engine |
| **Simulator Configs** | `Project_Simulator/configs.py` | Experiment parameters & seeds |
| **Experiment Drivers** | `Project_Simulator/run_experiments.py`, `run_e3.py`, `run_validation.py` | Generates all raw experiment data |
| **Plot Generation** | `Project_Simulator/plot_all.py` | Generates all publication-ready vector figures |
| **Simulation Results** | `Project_Simulator/results/` | Validation CSVs and experiment logs |
| **Figures** | `Project_Simulator/figures/` | Vector PDFs and PNG figures |
| **GPU Measurements** | `GPU_Measurements/measurements.csv`, `measurements_long.csv` | T4 GPU raw timing traces |
| **GPU Analysis & Manifest** | `GPU_Measurements/NAME3_GPU_Analysis/` | Calibration scripts, plots & summary CSVs |
| **Colab Sweep Traces** | `GPU_Measurements/colab_kaggle_sweep/` | 60 raw trial JSONs, prompts, diagnostics |
| **Phase 1 Submission** | `Phase1/phase1_final_report.pdf` (and `ms.pdf`) | Submitted 2-page report (3.5/5 score) |
| **Phase 2 Report Draft** | `Phase2/phase2_progress_report.tex` & `.pdf` | Working draft for 27 Oct submission |
| **Course Reference** | `Course_Context/` | Sample project descriptions & lecture knowledge base |
| **Professor Feedback Notes** | `docs/professor_feedback_notes.md` | Detailed breakdown of feedback & action plan |
| **Self-Contained Context** | `Context/` | Complete project handoff for AI agents |
