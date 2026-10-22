# 00 — Project Overview

## 1. Project Title & Concept
- **Title:** A Queueing-Network Simulator for an LLM Inference Serving Pipeline
- **Course:** E0 240: Modeling & Simulation
- **Department:** Computer Science and Automation (CSA) & Computational and Data Sciences (CDS)
- **Institution:** Indian Institute of Science (IISc), Bangalore
- **Instructor:** Prof. Sumit Kumar Mandal (skmandal@iisc.ac.in)

### Core Concept
Large Language Model (LLM) inference serving stacks (e.g., vLLM, Hugging Face TGI, TensorRT-LLM) process incoming user requests through multi-stage computational pipelines. User-perceived latency (Time to First Token - TTFT, and Inter-Token Latency - ITL) is fundamentally governed by queueing delays: request validation and tokenization, batch formation and scheduling delays, and hardware execution contention across parallel GPU decode workers.

Rather than running expensive, full-scale GPU cluster operator profiling (such as Vidur or FlexGen), this project models and simulates the serving stack as an open, discrete-time, three-station feedforward queueing network. The simulator is cycle-driven, verified analytically against discrete-time queueing closed forms, and calibrated using real Nvidia Tesla T4 GPU measurements.

---

## 2. Group Members

| Name | Student Registration (SR) No. | Department / Program |
|---|---|---|
| **Vaibhav Mahore** | 23631 | UG BTech (M&C), CSA |
| **Sujal Chavda** | 24288 | UG BTech (M&C), CSA |
| **Arindam Raina** | 25880 | Department of CSA |
| **Shreemaye Das** | 25958 | MTech, Department of CDS |

*All project submissions are joint team submissions representing all four members.*

---

## 3. Milestone Status & Key Deadlines

- **Phase 1 (Problem Statement & Validation Plan):**
  - Due: 22 September 2026 (Submitted as `ms.pdf`)
  - Evaluated / Returned: 07 October 2026
  - **Score Awarded:** **3.5 / 5.0** (70%)
  - Primary Feedback: Motivation for treating the pipeline as a queueing network was not entirely clear, and empirical experiments should be stronger with diverse models and queries.
- **Phase 2 (Progress Report & Empirical Results):**
  - **Deadline:** **27 October 2026 (11:59 PM)**
  - **Format:** IEEE Conference double-column format
  - **Page Limit:** **Strict maximum of 4 pages** (including all references, figures, and tables)
  - Core Goal: Strengthen motivation, expand analysis of preliminary results, and incorporate empirical GPU measurement calibrations.
- **Phase 3 (Final Report & Presentation):**
  - End of semester deliverable.
  - Full project report + final Beamer slide presentation.

---

## 4. The Three-Station Queueing Abstraction

The serving pipeline is modeled as an open, three-station feedforward queueing network where external requests arrive according to a Bernoulli process with parameter $\lambda \in (0, 0.5)$ requests/cycle:

```
[ External Arrivals ] 
        │ (Bernoulli λ)
        ▼
┌───────────────────────────────┐
│ Station 1 (Q1): Tokenizer     │  Single-server Geo/D/1
│                               │  Deterministic service time S1 = 2 cycles
│                               │  Models input validation, formatting & tokenization
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│ Station 2 (Q2): Batcher       │  FCFS Batch Aggregation Buffer
│                               │  Releases batch when B requests accumulate
│                               │  OR oldest request timer reaches τ cycles
└───────────────┬───────────────┘
                │ (Batch size ≤ B)
                ▼
┌───────────────────────────────┐
│ Station 3 (Q3): GPU Workers   │  Multi-server Geo/Geo/c parallel decode pool
│                               │  c homogeneous workers, each serving 1 batch
│                               │  Service time grounded in empirical GPU decode latency
└───────────────┬───────────────┘
                │
                ▼
         [ Departures / Done ]
```

### Station 1 ($Q_1$): Admission & Tokenizer
- **Queueing Type:** Single-server $Geo/D/1$ queue.
- **Service Time:** Fixed deterministic $S_1 = 2$ cycles per request ($\mu_1 = 0.5$).
- **Function:** Captures request admission, payload validation, prompt tokenization overhead, and formatting. Setting $S_1 = 2$ enables closed-form mathematical verification against discrete-time queueing theory.

### Station 2 ($Q_2$): Batching Scheduler
- **Queueing Type:** First-Come First-Served (FCFS) batch aggregation buffer with dual release triggers:
  1. **Batch Size Cap ($B$):** Releases when $B$ requests accumulate.
  2. **Timeout Threshold ($\tau$):** Releases if the head-of-line request has waited $\tau$ clock cycles.
- **Function:** Models static batching trade-offs. (With $B = 1$, $Q_2$ acts as a zero-delay pass-through buffer). Larger batch caps increase GPU compute efficiency but inflate queuing delay for early arrivals.

### Station 3 ($Q_3$): GPU Decode Workers
- **Queueing Type:** Multi-server pool of $c$ identical parallel workers ($Geo/Geo/c$ baseline, extensible to general empirical service distributions).
- **Service Time:** Variable token generation decode duration, where all requests within a batch execute synchronously. Baseline geometric completion probability $p_s = 1 / E[S_3]$.
- **Function:** Represents parallel GPU execution streams. Service parameters are calibrated against empirical Nvidia Tesla T4 GPU latency measurements across batch sizes $B \in \{1, \dots, 32\}$.
