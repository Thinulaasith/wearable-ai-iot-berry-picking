# Hierarchical Architecture With Other - XGBoost

## Combined Performance

**Accuracy:** 0.8588

**Macro F1:** 0.8038

**Weighted F1:** 0.8515

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.8400 | 0.5676 | 0.6774 | 37 |
| Idle | 0.7661 | 0.9314 | 0.8407 | 102 |
| Good Picking | 0.8000 | 0.8889 | 0.8421 | 36 |
| Bad Picking | 0.8235 | 0.5600 | 0.6667 | 50 |
| Pushing | 0.9839 | 1.0000 | 0.9919 | 122 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 21 | 15 | 1 | 0 | 0 |
| Idle | 1 | 95 | 0 | 6 | 0 |
| Good Picking | 2 | 0 | 32 | 0 | 2 |
| Bad Picking | 1 | 14 | 7 | 28 | 0 |
| Pushing | 0 | 0 | 0 | 0 | 122 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.5676 | 0.4054 | 0.0270 | 0.0000 | 0.0000 |
| Idle | 0.0098 | 0.9314 | 0.0000 | 0.0588 | 0.0000 |
| Good Picking | 0.0556 | 0.0000 | 0.8889 | 0.0000 | 0.0556 |
| Bad Picking | 0.0200 | 0.2800 | 0.1400 | 0.5600 | 0.0000 |
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

**Accuracy:** 0.9078

**Macro F1:** 0.8259

**Weighted F1:** 0.9026

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Good Picking | 0.8000 | 0.8889 | 0.8421 | 36 |
| Bad Picking | 0.8286 | 0.5800 | 0.6824 | 50 |
| Other | 0.9338 | 0.9732 | 0.9531 | 261 |

### Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking | Other |
|---|---:|---:|---:|
| Good Picking | 32 | 0 | 4 |
| Bad Picking | 7 | 29 | 14 |
| Other | 1 | 6 | 254 |

### Normalized Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking | Other |
|---|---:|---:|---:|
| Good Picking | 0.8889 | 0.0000 | 0.1111 |
| Bad Picking | 0.1400 | 0.5800 | 0.2800 |
| Other | 0.0038 | 0.0230 | 0.9732 |
