# 05 — Agent Instructions & Operating Directives

> [!IMPORTANT]
> **MANDATORY ONBOARDING DIRECTIVE FOR ALL AGENTS:**  
> **Any future prompt or agent working on this project MUST first read all files in this `Context/` folder before doing anything.**
> 
> Reading these documents provides immediate, complete grounding in the project context, technical architecture, feedback history, grading standards, and open tasks.

---

## 1. Prime Objective for Phase 2

The overarching goal of Phase 2 is to **elevate the project from a Phase 1 score of 3.5/5.0 to top marks** in the Phase 2 Progress Report (due **27 October 2026**, IEEE double-column format, maximum **4 pages**).

To achieve this, the agent must specifically address the two feedback items delivered by Prof. Sumit Kumar Mandal:
1. **Strengthen the Motivation for the Queueing Abstraction:**
   - Clearly explain why an open, three-station feedforward queueing model ($Q_1$ Tokenizer, $Q_2$ Batcher, $Q_3$ GPU Workers) is the right mathematical tool for LLM serving analysis.
   - Contrast our queueing simulator against full-scale GPU cluster operator profiling (e.g., Vidur, FlexGen): full profiling is computationally prohibitive for broad architectural exploration, whereas discrete-event queueing allows exploring thousands of scheduler configurations in seconds.
   - Decompose user-perceived QoS (TTFT, ITL) directly into queue waiting times ($W_{q,1}, W_{q,2}, W_{q,3}$) and service durations.
2. **Add Stronger, Multi-Model, and Hardware-Calibrated Analysis:**
   - Deeply integrate the empirical Tesla T4 GPU measurement campaign into the report.
   - Highlight the calibration split ($B \in \{1, 4, 16\}$) and held-out validation on $B \in \{2, 8, 32\}$ (demonstrating 4.43% MAPE).
   - Address model diversity: discuss how parameter scaling (e.g. 0.5B vs 1.5B vs 7B) affects decode step latency and batching gains.
   - Address query diversity: incorporate the uncapped length diagnostic ($KS = 0.3965$) showing that real generation lengths deviate from memoryless geometric distributions.

---

## 2. Guardrails & Behavioral Constraints

1. **Strict Page Budget:**
   - The Phase 2 report has a **hard ceiling of 4 pages** in standard IEEE conference double-column format.
   - Keep prose concise, prioritize high-information density tables and figures, and do not let references spill over to page 5.
2. **Authorship Integrity:**
   - The report must list all four verified group members and their SR numbers:
     - Vaibhav Mahore (23631)
     - Sujal Chavda (24288)
     - Arindam Raina (25880)
     - Shreemaye Das (25958)
   - Never reintroduce generic placeholders (`[Name (SR No.)]`).
3. **Preserve Validated Artifacts:**
   - Do NOT overwrite or modify verified simulation code in `Project_Simulator/` unless explicitly requested.
   - Do NOT regenerate or corrupt historical CSV results in `results/` or empirical GPU traces in `GPU_Measurements/`.
4. **Honesty About Completed vs. Pending Work:**
   - Be transparent: while GPU measurements are collected and held-out predictions achieve 4.43% MAPE, the formal `cycle_ms` millisecond-to-cycle mapping is pending Phase 2 finalization.
   - Do not claim that VIDUR code was executed (it was discussed as related literature).

---

## 3. Checklist for Future Work in Phase 2

- [ ] Read all files in `Context/` (`00` through `05`).
- [ ] Review `Phase2/phase2_progress_report.tex` against the 4-page IEEE limit.
- [ ] Incorporate the motivation figures and equations connecting TTFT/ITL to queueing delays.
- [ ] Embed the empirical GPU calibration table and held-out prediction plots from `GPU_Measurements/NAME3_GPU_Analysis/`.
- [ ] Discuss workload heterogeneity and model scaling implications.
- [ ] Compile LaTeX and verify that the output PDF is exactly 4 pages, cleanly formatted, with all 4 authors.
