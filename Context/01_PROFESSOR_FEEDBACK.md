# 01 — Professor Feedback & Course Expectations

## 1. Official Phase 1 Evaluation & Feedback

- **Course:** E0 240: Modeling & Simulation
- **Instructor:** Prof. Sumit Kumar Mandal (`skmandal@iisc.ac.in`, Office: CSA A359)
- **Phase 1 Submission:** `ms.pdf` (Submitted on 22 September 2026)
- **Returned Date:** Wednesday, October 7, 2026 at 12:02 PM
- **Score:** **3.5 / 5.0** (70%)
- **Evidence Screenshot:** Stored at `Phase1/Phase1_Feedback.jpeg`

### Verbatim Feedback from Instructor
> **1. Motivation behind treating it as queuing network is not clear entirely.**  
> **2. The experiment should have stronger. Different models, different queries etc should be considered.**

---

## 2. Summary of Email / Advisory Exchange with Prof. Sumit Kumar Mandal

Prior to and during the project iterations, communication with the instructor established key expectations for course project evaluations:

1. **Analytical Models are Necessary but Insufficient:**
   - In early discussions, the team considered validating the simulator purely against discrete-time closed forms ($Geo/D/1$, $Geo/Geo/1$).
   - The instructor explicitly signaled that theoretical toy models alone do not demonstrate research rigor. The simulator **must be validated against real-system data** — either through direct physical GPU profiling measurements or against an established standard systems simulator (such as VIDUR from MLSys '24).
2. **Grounding in Real Hardware (The "Why Real GPU Numbers?" Mandate):**
   - The instructor emphasized that modern systems modeling is valuable only if the queuing parameters (service times $E[S_3]$, batching scale factors, token generation dynamics) correspond to measurable hardware phenomena.
   - Simply picking arbitrary geometric parameters $E[S_3] = 20$ without demonstrating how they map to physical GPU execution times (milliseconds) on realistic models is insufficient for graduate-level modeling.
3. **Course Policy on Rigor & Deadlines:**
   - Strict deadline enforcement: *"Absolutely no extension of deadlines. Unfairness is a part of life unfortunately."*
   - Strict grading standard: Negative points will be awarded if an assignment score is high but project submissions lack research rigor. Projects are evaluated on **correctness, clarity, conciseness, and research rigor**.

---

## 3. What the Professor Specifically Wants for Phase 2

To turn the Phase 1 score of 3.5/5 into top marks in Phase 2, the team must explicitly address both feedback points:

### Requirement A: Crystal-Clear Motivation for the Queueing Network Abstraction
1. **Bridge Systems Reality and Queueing Theory:**
   - Explain why LLM serving (vLLM, Hugging Face TGI) is structurally a sequence of queues rather than a monolithic black-box compute kernel.
   - Show that user-perceived metrics (Time to First Token - TTFT, Inter-Token Latency - ITL) decompose directly into waiting time in the admission queue ($W_{q,1}$), batch formation buffer delay ($W_{q,2}$), and worker dispatch contention ($W_{q,3}$).
2. **The High Cost of Cluster Profiling vs. Value of Queueing Simulation:**
   - Full cluster trace replay (e.g. Vidur) requires massive GPU resources and extensive execution time.
   - An analytical and discrete-event queueing model allows system architects to explore thousands of scheduler configurations ($\tau, B, c, \lambda$) in seconds, uncovering stability boundaries ($\rho < 1$) and tail latency blowups analytically before cluster deployment.

### Requirement B: Stronger, Multi-Model, and Real-GPU Validated Experiments
1. **Validation Against Real GPU Numbers:**
   - Directly incorporate the empirical Tesla T4 GPU measurement campaign collected for Qwen 2.5-1.5B across batch sizes $B \in \{1, 2, 4, 8, 16, 32\}$.
   - Demonstrate the calibration/held-out validation methodology (calibrating on $B \in \{1, 4, 16\}$ and predicting on $B \in \{2, 8, 32\}$ with low MAPE).
   - Address the physical mapping between simulator clock cycles and physical execution milliseconds (`cycle_ms`).
2. **Workload and Model Diversity:**
   - Acknowledge and evaluate the impact of different model architectures (e.g., parameter scaling differences between 0.5B, 1.5B, and 7B models).
   - Address query heterogeneity: examine how variable prompt lengths and output sequence lengths challenge the memoryless geometric decode length assumption (incorporating the uncapped length diagnostic data where $KS = 0.3965$).
