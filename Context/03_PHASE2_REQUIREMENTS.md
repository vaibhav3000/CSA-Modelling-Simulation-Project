# 03 — Phase 2 Deliverable Requirements

## 1. Submission Overview

- **Milestone:** Phase 2 Progress Report
- **Course:** E0 240: Modeling & Simulation, IISc Bangalore
- **Submission Deadline:** **27 October 2026 (11:59 PM)**
- **Submission Channel:** Microsoft Teams / Course LMS (one submission per group)
- **File Format:** Single compiled PDF file compiled from standard IEEE LaTeX template

---

## 2. Strict Formatting Constraints

1. **Length Limit:** **Strict maximum of 4 pages** (all inclusive: text, figures, tables, appendices, and references).
   - Any page overflow past page 4 is strictly prohibited.
2. **Document Class & Layout:** Standard `IEEEtran` conference format:
   ```latex
   \documentclass[conference]{IEEEtran}
   ```
   - Two columns per page.
   - Standard 10 pt font, standard IEEE margins and spacing.
3. **Group Authorship:**
   - One joint submission per group.
   - All four team members and SR numbers must be clearly listed in the title author block:
     - **Vaibhav Mahore (23631)** — UG BTech (M&C), Dept of CSA
     - **Sujal Chavda (24288)** — UG BTech (M&C), Dept of CSA
     - **Arindam Raina (25880)** — Dept of CSA
     - **Shreemaye Das (25958)** — MTech, Dept of CDS
   - Do NOT use generic placeholders like `[Name (SR No.)]`.

---

## 3. Mandatory Content Sections

The Phase 2 report must expand significantly beyond the Phase 1 problem statement and provide detailed methodology and preliminary experimental results:

### Section I: Problem Statement & Motivation
- Formal statement of the LLM inference serving problem.
- **Direct response to Phase 1 Feedback:** Rigorous, explicit motivation for abstracting the LLM serving pipeline as a queueing network. Explain why simulation/analytical queueing is preferable to full-scale GPU profiling for architectural parameter exploration.
- Explicit definition of performance metrics: Time-to-First-Token (TTFT), Inter-Token Latency (ITL), queue occupancy ($L_q$), and queueing delay ($W_q$).

### Section II: Related Work
- Detailed comparison against prior LLM serving systems and simulators:
  - Memory management & scheduling: Orca (OSDI '22), vLLM (SOSP '23), FlexGen (ICML '23).
  - Cluster trace-based simulators: Vidur (MLSys '24).
  - Queueing theory foundations: Discrete-time queueing models (Haviv, Kleinrock).
- Clear differentiation showing our approach's unique speed and analytical tractability.

### Section III: Methodology & Model Formulation
- Mathematical formalization of the 3-station tandem queue:
  - $Q_1$ (Admission & Tokenizer): $Geo/D/1$, $S_1 = 2$ cycles.
  - $Q_2$ (Batching Scheduler): FCFS batch accumulation buffer with batch cap $B$ and timeout $\tau$.
  - $Q_3$ (Parallel GPU Workers): Multi-server $Geo/Geo/c$ decode engine with empirical service duration.
- Governing stability criteria: $\lambda < 0.5$ at $Q_1$, $\lambda E[S_3] / c < 1$ at $Q_3$.
- Flow conservation and discrete-time event-loop mechanics.

### Section IV: Analytical Validation (Layer 1)
- Quantitative verification against closed forms:
  - Deterministic service: $W_q = \rho(S-1)/(2(1-\rho))$, $L_q = \lambda^2 / (1 - 2\lambda)$ for $S = 2$.
  - Geometric service: Factor-of-2 variance penalty confirmation ($L_q = 2\lambda^2 / (1 - 2\lambda)$ for $E[S] = 2$).
  - Little's Law validation ($W = L_q / \lambda$) and convergence across simulation horizons ($10^3$ to $10^7$ cycles).
  - Verification goal: $<1\%$ error for all stable arrival rates $\lambda \le 0.45$.

### Section V: Significant Analysis of Preliminary Results (Layer 2 & Experiments)
- **Direct response to Phase 1 Feedback (Stronger Experiments):**
  - **Empirical GPU Grounding:** Hardware measurement data on Tesla T4 across batch sizes $B \in \{1, \dots, 32\}$ using Qwen 2.5-1.5B.
  - **Held-Out Model Calibration:** Power-law fit on $B \in \{1, 4, 16\}$ predicting held-out batch sizes $B \in \{2, 8, 32\}$ with $<15\%$ MAPE (achieved 4.43% MAPE).
  - **Max-Length vs. Linear Predictor:** Analysis showing response length drives decode latency ($r = 0.9493$).
  - **Worker Scaling & Parallelism:** Experiment E2 showing latency reductions and queue stabilization when scaling workers from $c = 1$ to $c = 2$.
  - **Batching Trade-Off Frontier:** Experiment E3 mapping the Pareto curve across batch capacities $B$ and timeout thresholds $\tau$.
  - Discussion of model scaling (0.5B vs 1.5B vs larger architectures) and prompt/generation length heterogeneity.
