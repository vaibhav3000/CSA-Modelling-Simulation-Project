# Professor Feedback Notes & Phase 2 Action Plan

**Course:** E0 240: Modeling & Simulation  
**Institution:** Department of Computer Science & Automation (CSA), Indian Institute of Science (IISc), Bangalore  
**Project:** A Queueing-Network Simulator for an LLM Inference Serving Pipeline  
**Group Members:**
- Vaibhav Mahore (SR No. 23631)
- Sujal Chavda (SR No. 24288)
- Arindam Raina (SR No. 25880)
- Shreemaye Das (SR No. 25958)

---

## 1. Phase 1 Evaluation Summary

- **Submission:** `ms.pdf` (submitted 22 September 2026)
- **Returned:** Wednesday, October 7, 2026 at 12:02 PM
- **Score Awarded:** **3.5 / 5.0** (70%)
- **Feedback Reference:** `Phase1/Phase1_Feedback.jpeg` (captured from course LMS)

---

## 2. Verbatim Feedback from Instructor

> **1. Motivation behind treating it as queuing network is not clear entirely.**  
> **2. The experiment should have stronger. Different models, different queries etc should be considered.**

---

## 3. In-Depth Diagnosis & Gap Analysis

### Feedback Item 1: Motivation for the Queueing Network Abstraction
* **Current State in Phase 1:**  
  The Phase 1 problem statement introduced the 3-station pipeline (Tokenizer $\to$ Batch Scheduler $\to$ GPU Workers) and stated that user-perceived latency is dominated by queueing delay. However, it jumped rapidly to formal queueing equations without sufficiently connecting modern LLM serving architecture (vLLM, Orca, Triton) to fundamental queueing phenomena.
* **Why the Instructor Flagged This:**  
  LLM serving is often analyzed from a systems / kernel optimization perspective (e.g., PagedAttention, KV-cache offloading, FlashAttention). The report must explicitly justify **why a queueing abstraction is necessary and uniquely advantageous**:
  1. *Decoupling compute scheduling from operator profiling:* Profiling entire transformer kernels (Vidur, FlexGen) requires expensive hardware clusters. Queueing theory allows evaluating architectural trade-offs (batching timeouts, admission control, worker sizing) analytically and via discrete-event simulation at negligible computational cost.
  2. *End-to-End Latency Breakdown:* User experience (Time to First Token - TTFT, and Inter-Token Latency - ITL) is fundamentally a sum of queueing delays across distinct stages:
     - $Q_1$ (Admission/Validation): Fixed tokenization delay + request queuing ($Geo/D/1$).
     - $Q_2$ (Batching Scheduler): Waiting time for batch aggregation ($B$ requests or timeout $\tau$).
     - $Q_3$ (GPU Execution): Contention delay for parallel worker slots ($Geo/Geo/c$ or general service distributions).
  3. *Throughput vs. Latency Pareto Frontier:* Queueing network analysis mathematically characterizes the trade-off where larger batch sizes increase GPU utilization but induce queue buildup and tail latency inflation.

### Feedback Item 2: Empirical Rigor & Experimental Breadth
* **Current State in Phase 1:**  
  The initial empirical grounding relied on a single model (`Qwen/Qwen2.5-1.5B-Instruct`) measured on a single hardware target (Nvidia Tesla T4) using homogeneous sample queries and a single geometric service fit ($E[S_3] = 20$).
* **Why the Instructor Flagged This:**  
  1. *Model Diversity:* Serving dynamics differ significantly across model parameter scales (e.g., 0.5B vs. 1.5B vs. 3B/7B). Decode step latencies scale with parameter count and weight memory bandwidth, shifting the balance between batching overhead and compute efficiency.
  2. *Query & Workload Diversity:* Fixed prompt lengths do not reflect real serving distributions. Real workloads (e.g., ShareGPT, GSM8K, MT-Bench) feature heavy-tailed prompt lengths and bimodal or multi-modal output generation lengths.
  3. *Validation Coverage:* Need stronger empirical-to-simulation cross-validation showing how calibration coefficients generalize to unseen batch sizes, prompt distributions, and timeout thresholds.

---

## 4. Phase 2 Roadmap & Action Items

**Phase 2 Deadline:** 27 October 2026 (11:59 PM)  
**Deliverable Format:** IEEE Conference double-column format, maximum 4 pages.

### Action Plan for Phase 2 Report

1. **Strengthen Section I & II (Serving Architecture $\to$ Queueing Abstraction):**
   - Provide an architectural diagram explicitly mapping the physical stages of vLLM / Hugging Face TGI to the queueing stations $Q_1, Q_2, Q_3$.
   - Formulate the exact mathematical relationship connecting TTFT and ITL to $W_{q,1}$, $W_{q,2}$, and $W_{q,3}$.
   - Clarify the difference between static batching and continuous/iteration-level batching.

2. **Broaden Empirical GPU Grounding:**
   - Incorporate multiple model configurations (e.g., Qwen 2.5-0.5B, Qwen 2.5-1.5B) or compare parameter scaling effects.
   - Analyze heterogeneous prompt/generation lengths (short conversational queries vs. long synthetic contexts).
   - Evaluate empirical CDFs of decode lengths against Geometric vs. Pareto / Log-Normal service approximations.

3. **Expanded Simulation Experiments (Section IV & V):**
   - **Experiment E1 (Validation):** Sweep arrival rate $\lambda \in [0.05, 0.49]$ across run lengths $10^3$ to $10^7$ cycles, verifying $<1\%$ deviation against $Geo/D/1$ and $Geo/Geo/1$ closed forms.
   - **Experiment E2 (Pipeline & Parallelism):** Evaluate end-to-end delay $W_{e2e}$ and queue occupancy $L_q$ across worker counts $c \in \{1, 2, 4\}$.
   - **Experiment E3 (Batching Trade-Offs):** Map the 2D parameter space of batch cap $B \in \{1, 4, 8, 16, 32\}$ and timeout timer $\tau \in \{1, 2, 5, 10, 20\}$ at varying injection loads $\lambda$.
   - **Layer-2 Hardware Calibration:** Validate GPU batch time prediction on held-out test splits with MAPE $< 15\%$.

4. **Formatting & Quality Control:**
   - Ensure complete team author block: Vaibhav Mahore (23631), Sujal Chavda (24288), Arindam Raina (25880), Shreemaye Das (25958).
   - Maintain strict 4-page ceiling in IEEE conference double-column format.
