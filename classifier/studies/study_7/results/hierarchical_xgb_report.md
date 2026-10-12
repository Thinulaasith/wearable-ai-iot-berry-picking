# Standard Hierarchical Architecture - XGBoost

## Combined Performance

**Accuracy:** 0.8530

**Macro F1:** 0.7961

**Weighted F1:** 0.8458

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.9524 | 0.5405 | 0.6897 | 37 |
| Idle | 0.7750 | 0.9118 | 0.8378 | 102 |
| Good Picking | 0.7500 | 0.9167 | 0.8250 | 36 |
| Bad Picking | 0.7368 | 0.5600 | 0.6364 | 50 |
| Pushing | 0.9839 | 1.0000 | 0.9919 | 122 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 20 | 15 | 1 | 1 | 0 |
| Idle | 0 | 93 | 0 | 9 | 0 |
| Good Picking | 1 | 0 | 33 | 0 | 2 |
| Bad Picking | 0 | 12 | 10 | 28 | 0 |
| Pushing | 0 | 0 | 0 | 0 | 122 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.5405 | 0.4054 | 0.0270 | 0.0270 | 0.0000 |
| Idle | 0.0000 | 0.9118 | 0.0000 | 0.0882 | 0.0000 |
| Good Picking | 0.0278 | 0.0000 | 0.9167 | 0.0000 | 0.0556 |
| Bad Picking | 0.0000 | 0.2400 | 0.2000 | 0.5600 | 0.0000 |
| Pushing | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |

## Stage 1 — Activity Classification

**Accuracy:** 0.8818

**Macro F1:** 0.8412

**Weighted F1:** 0.8780

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.9524 | 0.5405 | 0.6897 | 37 |
| Idle | 0.7750 | 0.9118 | 0.8378 | 102 |
| Picking | 0.8659 | 0.8256 | 0.8452 | 86 |
| Pushing | 0.9839 | 1.0000 | 0.9919 | 122 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Picking | Pushing |
|---|---:|---:|---:|---:|
| Bending | 20 | 15 | 2 | 0 |
| Idle | 0 | 93 | 9 | 0 |
| Picking | 1 | 12 | 71 | 2 |
| Pushing | 0 | 0 | 0 | 122 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Picking | Pushing |
|---|---:|---:|---:|---:|
| Bending | 0.5405 | 0.4054 | 0.0541 | 0.0000 |
| Idle | 0.0000 | 0.9118 | 0.0882 | 0.0000 |
| Picking | 0.0116 | 0.1395 | 0.8256 | 0.0233 |
| Pushing | 0.0000 | 0.0000 | 0.0000 | 1.0000 |

## Stage 2 — Picking Classification

**Accuracy:** 0.8721

**Macro F1:** 0.8719

**Weighted F1:** 0.8727

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Good Picking | 0.7660 | 1.0000 | 0.8675 | 36 |
| Bad Picking | 1.0000 | 0.7800 | 0.8764 | 50 |

### Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking |
|---|---:|---:|
| Good Picking | 36 | 0 |
| Bad Picking | 11 | 39 |

### Normalized Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking |
|---|---:|---:|
| Good Picking | 1.0000 | 0.0000 |
| Bad Picking | 0.2200 | 0.7800 |
