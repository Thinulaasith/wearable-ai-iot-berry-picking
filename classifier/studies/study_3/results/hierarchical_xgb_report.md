# Standard Hierarchical Architecture - XGBoost

## Combined Performance

**Accuracy:** 0.8489

**Macro F1:** 0.7875

**Weighted F1:** 0.8414

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.8723 | 0.5467 | 0.6721 | 75 |
| Idle | 0.7782 | 0.9118 | 0.8397 | 204 |
| Good Picking | 0.7303 | 0.9028 | 0.8075 | 72 |
| Bad Picking | 0.7397 | 0.5400 | 0.6243 | 100 |
| Pushing | 0.9879 | 1.0000 | 0.9939 | 244 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 41 | 31 | 1 | 2 | 0 |
| Idle | 3 | 186 | 0 | 15 | 0 |
| Good Picking | 2 | 0 | 65 | 2 | 3 |
| Bad Picking | 1 | 22 | 23 | 54 | 0 |
| Pushing | 0 | 0 | 0 | 0 | 244 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.5467 | 0.4133 | 0.0133 | 0.0267 | 0.0000 |
| Idle | 0.0147 | 0.9118 | 0.0000 | 0.0735 | 0.0000 |
| Good Picking | 0.0278 | 0.0000 | 0.9028 | 0.0278 | 0.0417 |
| Bad Picking | 0.0100 | 0.2200 | 0.2300 | 0.5400 | 0.0000 |
| Pushing | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |

## Stage 1 — Activity Classification

**Accuracy:** 0.8849

**Macro F1:** 0.8420

**Weighted F1:** 0.8813

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.8723 | 0.5467 | 0.6721 | 75 |
| Idle | 0.7782 | 0.9118 | 0.8397 | 204 |
| Picking | 0.8889 | 0.8372 | 0.8623 | 172 |
| Pushing | 0.9879 | 1.0000 | 0.9939 | 244 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Picking | Pushing |
|---|---:|---:|---:|---:|
| Bending | 41 | 31 | 3 | 0 |
| Idle | 3 | 186 | 15 | 0 |
| Picking | 3 | 22 | 144 | 3 |
| Pushing | 0 | 0 | 0 | 244 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Picking | Pushing |
|---|---:|---:|---:|---:|
| Bending | 0.5467 | 0.4133 | 0.0400 | 0.0000 |
| Idle | 0.0147 | 0.9118 | 0.0735 | 0.0000 |
| Picking | 0.0174 | 0.1279 | 0.8372 | 0.0174 |
| Pushing | 0.0000 | 0.0000 | 0.0000 | 1.0000 |

## Stage 2 — Picking Classification

**Accuracy:** 0.8547

**Macro F1:** 0.8544

**Weighted F1:** 0.8554

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Good Picking | 0.7527 | 0.9722 | 0.8485 | 72 |
| Bad Picking | 0.9747 | 0.7700 | 0.8603 | 100 |

### Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking |
|---|---:|---:|
| Good Picking | 70 | 2 |
| Bad Picking | 23 | 77 |

### Normalized Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking |
|---|---:|---:|
| Good Picking | 0.9722 | 0.0278 |
| Bad Picking | 0.2300 | 0.7700 |
