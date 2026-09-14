# Standard Hierarchical Architecture - Random Forest

## Combined Performance

**Accuracy:** 0.8623

**Macro F1:** 0.7641

**Weighted F1:** 0.8452

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.9286 | 0.6500 | 0.7647 | 20 |
| Idle | 0.9280 | 0.9508 | 0.9393 | 122 |
| Good Picking | 0.5806 | 1.0000 | 0.7347 | 36 |
| Bad Picking | 0.7143 | 0.2885 | 0.4110 | 52 |
| Pushing | 0.9433 | 1.0000 | 0.9708 | 133 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 13 | 0 | 3 | 0 | 4 |
| Idle | 0 | 116 | 0 | 6 | 0 |
| Good Picking | 0 | 0 | 36 | 0 | 0 |
| Bad Picking | 1 | 9 | 23 | 15 | 4 |
| Pushing | 0 | 0 | 0 | 0 | 133 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.6500 | 0.0000 | 0.1500 | 0.0000 | 0.2000 |
| Idle | 0.0000 | 0.9508 | 0.0000 | 0.0492 | 0.0000 |
| Good Picking | 0.0000 | 0.0000 | 1.0000 | 0.0000 | 0.0000 |
| Bad Picking | 0.0192 | 0.1731 | 0.4423 | 0.2885 | 0.0769 |
| Pushing | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |

## Stage 1 — Activity Classification

**Accuracy:** 0.9256

**Macro F1:** 0.8851

**Weighted F1:** 0.9233

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.9286 | 0.6500 | 0.7647 | 20 |
| Idle | 0.9280 | 0.9508 | 0.9393 | 122 |
| Picking | 0.8916 | 0.8409 | 0.8655 | 88 |
| Pushing | 0.9433 | 1.0000 | 0.9708 | 133 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Picking | Pushing |
|---|---:|---:|---:|---:|
| Bending | 13 | 0 | 3 | 4 |
| Idle | 0 | 116 | 6 | 0 |
| Picking | 1 | 9 | 74 | 4 |
| Pushing | 0 | 0 | 0 | 133 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Picking | Pushing |
|---|---:|---:|---:|---:|
| Bending | 0.6500 | 0.0000 | 0.1500 | 0.2000 |
| Idle | 0.0000 | 0.9508 | 0.0492 | 0.0000 |
| Picking | 0.0114 | 0.1023 | 0.8409 | 0.0455 |
| Pushing | 0.0000 | 0.0000 | 0.0000 | 1.0000 |

## Stage 2 — Picking Classification

**Accuracy:** 0.7045

**Macro F1:** 0.7007

**Weighted F1:** 0.6945

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Good Picking | 0.5806 | 1.0000 | 0.7347 | 36 |
| Bad Picking | 1.0000 | 0.5000 | 0.6667 | 52 |

### Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking |
|---|---:|---:|
| Good Picking | 36 | 0 |
| Bad Picking | 26 | 26 |

### Normalized Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking |
|---|---:|---:|
| Good Picking | 1.0000 | 0.0000 |
| Bad Picking | 0.5000 | 0.5000 |
