# E0240 Project 1: A Queueing-Network Simulator for an LLM Inference Serving Pipeline

**Course:** E0 240: Modeling & Simulation  
**Department:** Computer Science & Automation (CSA) / Computational & Data Sciences (CDS)  
**Institution:** Indian Institute of Science (IISc), Bangalore  
**Instructor:** Prof. Sumit K. Mandal  

---

## 👥 Group Members

| Name | SR Number | Department / Degree Program |
|---|---|---|
| **Vaibhav Mahore** | 23631 | UG BTech (M&C), CSA |
| **Sujal Chavda** | 24288 | UG BTech (M&C), CSA |
| **Arindam Raina** | 25880 | Department of CSA |
| **Shreemaye Das** | 25958 | MTech, CDS |

---

## 📋 Course Milestones & Status

| Phase | Milestone Description | Deadline / Return Date | Status / Notes |
|---|---|---|---|
| **Phase 1** | Problem Statement & Validation Plan (2 pages) | Submitted 22 Sep 2026<br>Returned 07 Oct 2026 | **Score: 3.5 / 5.0** (See [feedback notes](file:///c:/Users/vaibhav%20mahore/Downloads/CSA%20Modelling%20Simulation/Project/E0240-Project1/docs/professor_feedback_notes.md) and [feedback screenshot](file:///c:/Users/vaibhav%20mahore/Downloads/CSA%20Modelling%20Simulation/Project/E0240-Project1/Phase1/Phase1_Feedback.jpeg)) |
| **Phase 2** | Progress Report & Core Simulation Experiments | **27 October 2026 (11:59 PM)** | Target: **IEEE double-column format, maximum 4 pages** |
| **Phase 3** | Final Report & Final Presentation | End of semester | Complete codebase & Beamer slides available in repository |

---

## 📖 Project Overview

Large Language Model (LLM) serving systems (such as vLLM, TensorRT-LLM, and Hugging Face TGI) process requests through multi-stage pipelines subject to arrival bursts and variable token lengths. In this project, we develop a cycle-driven, discrete-time queueing-network simulator that models the serving pipeline as a three-station feedforward chain:

1. **Station 1 ($Q_1$ - Admission & Tokenization):** Deterministic single-server queue ($Geo/D/1$, $S_1 = 2$ cycles) capturing input sanitization, tokenization, and admission checks.
2. **Station 2 ($Q_2$ - Batching Scheduler):** First-Come First-Served (FCFS) aggregation buffer releasing batches when either capacity $B$ is reached or the oldest request has waited $\tau$ cycles.
3. **Station 3 ($Q_3$ - GPU Parallel Decode Workers):** Multi-server pool ($Geo/Geo/c$) serving batched requests simultaneously, with service durations grounded in empirical Nvidia Tesla T4 GPU measurements.

### Key Features
- **Rigorous Multi-Layer Validation:** Verified analytically against discrete-time closed forms ($Geo/D/1$, $Geo/Geo/1$) with $<1\%$ error over $10^7$ cycle simulation runs.
- **Hardware-Calibrated Parameters:** Empirically grounded using real GPU inference benchmarks across batch sizes $B \in \{1, 2, 4, 8, 16, 32\}$ on `Qwen/Qwen2.5-1.5B-Instruct`.
- **Parametric Scheduler Sweeps:** Fast simulation mapping the Pareto trade-off between batch size, timeout threshold, queue occupancy, and end-to-end user latency.

---

## 📁 Repository Structure

```text
CSA-Modelling-Simulation-Project/
├── README.md                              # This file
├── Context/                               # Self-contained project knowledge base & agent onboarding
│   ├── 00_PROJECT_OVERVIEW.md             # Project premise, 3 stations (Q1, Q2, Q3), team members & dates
│   ├── 01_PROFESSOR_FEEDBACK.md           # Phase 1 evaluation, email exchange & professor requirements
│   ├── 02_CURRENT_STATUS.md               # Completed simulation & GPU work, pending items & key file links
│   ├── 03_PHASE2_REQUIREMENTS.md          # 4-page IEEE double-column requirements & content sections
│   ├── 04_KEY_FILES_MAP.md                # Rapid physical file locator map
│   └── 05_AGENT_INSTRUCTIONS.md           # Mandatory directives and guidelines for future AI agents
├── Phase1/                                # Phase 1 submission package
│   ├── phase1_final_report.tex            # Submitted IEEE conference LaTeX source
│   ├── phase1_final_report.pdf            # Submitted IEEE version with verified author names
│   ├── ms.pdf                             # Original submitted PDF (identical to phase1_final_report.pdf)
│   ├── phase1_refs.bib                    # BibTeX bibliography file
│   └── Phase1_Feedback.jpeg               # Instructor feedback & score screenshot
├── Phase2/                                # Phase 2 progress report files
│   ├── phase2_progress_report.tex         # Phase 2 LaTeX source (target: max 4 pages IEEE)
│   └── phase2_progress_report.pdf         # Compiled Phase 2 progress report
├── Phase3/                                # Phase 3 deliverables & presentation
│   ├── phase3_final_report.tex            # Final report LaTeX source
│   ├── phase3_final_report.pdf            # Final report PDF
│   ├── phase3_presentation_beamer_v4.tex  # Beamer slide presentation source
│   └── phase3_presentation_beamer_v4.pdf  # Final presentation PDF
├── Project_Simulator/                     # Core simulation engine and tooling
│   ├── network_sim.py                     # Discrete-time cycle-driven queueing simulator
│   ├── configs.py                         # Experiment parameters and network configurations
│   ├── run_experiments.py                # Main experiment runner (E1, E2, E3 sweeps)
│   ├── run_validation.py                 # Closed-form theoretical validation suite
│   ├── run_e3.py                          # Dedicated batching scheduler parameter sweep
│   ├── plot_all.py                        # Automated publication-quality figure generator
│   ├── check_conventions.py               # Repository conventions and reproducibility validator
│   ├── make_beamer_figures_v2.py          # Figure generator for presentation slides
│   ├── make_beamer_figures_v3.py          # Additional presentation figure generator
│   ├── build_presentation_beamer.sh       # Script to compile Beamer presentation
│   ├── figures/                           # Generated plots (PNG and vector PDF)
│   └── results/                           # Raw simulation CSV outputs and run logs
├── GPU_Measurements/                      # Empirical hardware calibration data
│   ├── measurements.csv                   # Tesla T4 GPU batch execution measurements
│   ├── measurements_long.csv              # Long-run GPU benchmark logs
│   ├── NAME3_GPU_Analysis/                # Empirical scaling analysis, diagnostics, and plots
│   └── colab_kaggle_sweep/                # Google Colab / Kaggle benchmark sweep trials and JSONs
├── Course_Context/                        # Reference materials and course problem specs
│   ├── list_of_sample_projects.pdf        # Official course project descriptions
│   ├── PROJECT1_COURSE_MINING_REPORT.md   # Detailed course problem analysis
│   ├── COURSE_KNOWLEDGE_BASE.md           # Modeling & simulation theoretical foundation
│   ├── single_queue_simulation_geo_d_1.m  # Reference MATLAB implementation
│   └── top_script.m                       # Reference MATLAB driver
├── docs/                                  # Project documentation & review notes
│   └── professor_feedback_notes.md        # Detailed breakdown of Phase 1 feedback and Phase 2 action items
└── Archive/                               # Preserved legacy directories (00_, 01_, 02_, etc.), zips & old drafts
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- `numpy`, `pandas`, `matplotlib`, `scipy`

### Running the Simulator
```bash
cd Project_Simulator

# Run analytical closed-form validation
python run_validation.py

# Run pipeline experiments (E1, E2)
python run_experiments.py

# Run batching trade-off sweep (E3)
python run_e3.py

# Generate all figures
python plot_all.py
```
