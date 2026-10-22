# NAME 3 GPU Analysis

This folder contains the GPU measurements and NAME 3 analysis generated during the validation work.

## Contents
- `measurements_kaggle_export.csv`: Kaggle raw measurement export available in the working set; this copy contains B={1,2,4,8}.
- `measurements_long_kaggle_export.csv`: sequence-level companion export for B={1,2,4,8}.
- `length_diagnostic.csv`: 100-prompt uncapped (512 max_new_tokens) length diagnostic; 0/100 hit the cap.
- `structural_test.csv`: uncapped structural batching diagnostic, 5 trials for each B in {1,2,4,8,16,32}.
- `name3_heldout_validation.csv`: held-out latency/throughput comparison using calibration B={1,4,16} and held-out B={2,8,32}.
- `name3_summary.csv`: summary metrics from the NAME 3 analysis.
- `gpu_batch_time.png`: real-GPU generation time versus batch size.
- `geometric_cdf_comparison.png`: observed versus fitted geometric sequence-length CDF from the uncapped diagnostic.

## Current key results
- Geometric KS distance: 0.3965
- corr(time, B): 0.7384
- corr(time, max sequence length): 0.9493
- Linear-in-B held-out latency MAPE: 15.25%
- Max-length held-out latency MAPE: 9.14%
- Linear-in-B held-out throughput MAPE: 17.60%
- Max-length held-out throughput MAPE: 10.75%

## Notebook
Kaggle notebook: https://www.kaggle.com/code/sujalchavda/notebook7ea0efa30b

## Important pending item
The final simulator cycle-to-milliseconds mapping and the corresponding calibration of the simulator's cycle-based Q3 service parameters were not finalized in this analysis set.
