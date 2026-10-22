# 04 — Key Files & Directory Map

This guide provides a rapid reference to the exact physical locations of all core artifacts within `CSA-Modelling-Simulation-Project/`.

---

## 1. Directory Overview

| Component | Directory Path | Primary Purpose |
|---|---|---|
| **Context & Onboarding** | `Context/` | Self-contained project knowledge base for AI agents & contributors |
| **Phase 1 Package** | `Phase1/` | Submitted Phase 1 IEEE report, bibtex, feedback screenshot |
| **Phase 2 Package** | `Phase2/` | Working LaTeX source and compiled PDF for Phase 2 (due 27 Oct 2026) |
| **Phase 3 Package** | `Phase3/` | Final report source and Beamer presentation slides |
| **Simulator Engine & Scripts** | `Project_Simulator/` | Core discrete-event queueing simulation code & figure generators |
| **Simulation Results** | `Project_Simulator/results/` | Raw CSV outputs from validation runs and experiments E2/E3 |
| **Generated Figures** | `Project_Simulator/figures/` | Publication-ready vector PDF and PNG plots |
| **GPU Measurement Data** | `GPU_Measurements/` | Empirical Tesla T4 GPU traces, calibration fits & Kaggle sweeps |
| **Course Reference** | `Course_Context/` | Course syllabus, project requirements & MATLAB reference scripts |
| **Professor Review Notes** | `docs/` | Detailed evaluation breakdown and actionable Phase 2 checklist |
| **Historical Archive** | `Archive/` | Preserved legacy directories (00_, 01_, 02_, etc.), zips & old drafts |

---

## 2. Key File Locations

### Core Simulator Code (`Project_Simulator/`)
- `network_sim.py`: Core discrete-event 3-station tandem queueing engine.
- `configs.py`: Network parameter configurations, random seeds, and experiment setups.
- `run_validation.py`: Analytical validation script (tests $Geo/D/1$, $Geo/Geo/1$, factor-2 variance penalty).
- `run_experiments.py`: Runs experiment E2 (worker pool scaling and delay analysis).
- `run_e3.py`: Runs experiment E3 (batch capacity $B$ and timeout $\tau$ trade-off sweep).
- `plot_all.py`: Generates all publication-quality vector plots for reports and slides.
- `check_conventions.py`: Linter and convention validator for simulation outputs.

### Simulation Outputs (`Project_Simulator/results/`)
- `validation_table.csv`: Comprehensive theoretical vs. simulated metrics across run lengths.
- `validation_geo_d_1_S2.csv`: Analytical validation points for deterministic service ($S = 2$).
- `validation_factor2.csv`: Verification points for geometric service factor-2 penalty.
- `experiment_e2_pipeline.csv`: Raw results for worker scaling ($c \in \{1, 2\}$) across arrival rates.
- `experiment_e3_batching.csv`: Raw results for batch size $B$ and timeout $\tau$ sweeps.

### GPU Hardware Traces (`GPU_Measurements/`)
- `measurements.csv`: Raw execution times for batched inference on Nvidia Tesla T4 GPU.
- `measurements_long.csv`: Extended GPU measurement traces.
- `NAME3_GPU_Analysis/`:
  - `name3_summary.csv`: Summary of linear-in-$B$ vs. max-sequence-length latency models.
  - `name3_heldout_validation.csv`: Prediction errors on held-out batch sizes $\{2, 8, 32\}$.
  - `length_diagnostic.csv`: Uncapped 512-token response length empirical distribution ($KS = 0.3965$).
  - `batch_time_vs_max_length.png`: Correlation plot between batch time and maximum sequence length.
  - `gpu_batch_time.png`: GPU execution latency vs. batch size scaling curve.
- `colab_kaggle_sweep/`:
  - `sweep_20260920T132814Z_96c7e45f/`: 60 trial JSON files (`trial_B*.json`) across $B \in \{1, 2, 4, 8, 16, 32\}$, `tokenizer_trials.csv`, and `calibration_parameters.json`.

### Deliverables & Reports
- **Phase 1 Report:** `Phase1/phase1_final_report.pdf` (submitted version with all 4 member names).
- **Phase 1 LaTeX:** `Phase1/phase1_final_report.tex` and bibliography `Phase1/phase1_refs.bib`.
- **Phase 1 Feedback Image:** `Phase1/Phase1_Feedback.jpeg` (screenshot showing 3.5/5 score).
- **Phase 2 Working Draft:** `Phase2/phase2_progress_report.tex` and `Phase2/phase2_progress_report.pdf`.
- **Phase 3 Presentation:** `Phase3/phase3_presentation_beamer_v4.pdf`.
