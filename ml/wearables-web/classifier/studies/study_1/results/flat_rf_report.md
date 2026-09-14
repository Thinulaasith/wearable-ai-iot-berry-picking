# Flat Architecture - Random Forest

## Final Performance

**Accuracy:** 0.8650

**Macro F1:** 0.7563

**Weighted F1:** 0.8450

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.8125 | 0.6500 | 0.7222 | 20 |
| Idle | 0.9291 | 0.9672 | 0.9478 | 122 |
| Good Picking | 0.5806 | 1.0000 | 0.7347 | 36 |
| Bad Picking | 0.8235 | 0.2692 | 0.4058 | 52 |
| Pushing | 0.9433 | 1.0000 | 0.9708 | 133 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 13 | 0 | 3 | 0 | 4 |
| Idle | 1 | 118 | 0 | 3 | 0 |
| Good Picking | 0 | 0 | 36 | 0 | 0 |
| Bad Picking | 2 | 9 | 23 | 14 | 4 |
| Pushing | 0 | 0 | 0 | 0 | 133 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.6500 | 0.0000 | 0.1500 | 0.0000 | 0.2000 |
| Idle | 0.0082 | 0.9672 | 0.0000 | 0.0246 | 0.0000 |
| Good Picking | 0.0000 | 0.0000 | 1.0000 | 0.0000 | 0.0000 |
| Bad Picking | 0.0385 | 0.1731 | 0.4423 | 0.2692 | 0.0769 |
| Pushing | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |
