# Standard Hierarchical Architecture - XGBoost

## Combined Performance

**Accuracy:** 0.8650

**Macro F1:** 0.7577

**Weighted F1:** 0.8465

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.8667 | 0.6500 | 0.7429 | 20 |
| Idle | 0.9291 | 0.9672 | 0.9478 | 122 |
| Good Picking | 0.5625 | 1.0000 | 0.7200 | 36 |
| Bad Picking | 0.7778 | 0.2692 | 0.4000 | 52 |
| Pushing | 0.9568 | 1.0000 | 0.9779 | 133 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 13 | 0 | 4 | 0 | 3 |
| Idle | 0 | 118 | 0 | 4 | 0 |
| Good Picking | 0 | 0 | 36 | 0 | 0 |
| Bad Picking | 2 | 9 | 24 | 14 | 3 |
| Pushing | 0 | 0 | 0 | 0 | 133 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.6500 | 0.0000 | 0.2000 | 0.0000 | 0.1500 |
| Idle | 0.0000 | 0.9672 | 0.0000 | 0.0328 | 0.0000 |
| Good Picking | 0.0000 | 0.0000 | 1.0000 | 0.0000 | 0.0000 |
| Bad Picking | 0.0385 | 0.1731 | 0.4615 | 0.2692 | 0.0577 |
| Pushing | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |

## Stage 1 — Activity Classification

**Accuracy:** 0.9311

**Macro F1:** 0.8848

**Weighted F1:** 0.9288

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.8667 | 0.6500 | 0.7429 | 20 |
| Idle | 0.9291 | 0.9672 | 0.9478 | 122 |
| Picking | 0.9024 | 0.8409 | 0.8706 | 88 |
| Pushing | 0.9568 | 1.0000 | 0.9779 | 133 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Picking | Pushing |
|---|---:|---:|---:|---:|
| Bending | 13 | 0 | 4 | 3 |
| Idle | 0 | 118 | 4 | 0 |
| Picking | 2 | 9 | 74 | 3 |
| Pushing | 0 | 0 | 0 | 133 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Picking | Pushing |
|---|---:|---:|---:|---:|
| Bending | 0.6500 | 0.0000 | 0.2000 | 0.1500 |
| Idle | 0.0000 | 0.9672 | 0.0328 | 0.0000 |
| Picking | 0.0227 | 0.1023 | 0.8409 | 0.0341 |
| Pushing | 0.0000 | 0.0000 | 0.0000 | 1.0000 |

## Stage 2 — Picking Classification

**Accuracy:** 0.6364

**Macro F1:** 0.6239

**Weighted F1:** 0.6115

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Good Picking | 0.5294 | 1.0000 | 0.6923 | 36 |
| Bad Picking | 1.0000 | 0.3846 | 0.5556 | 52 |

### Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking |
|---|---:|---:|
| Good Picking | 36 | 0 |
| Bad Picking | 32 | 20 |

### Normalized Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking |
|---|---:|---:|
| Good Picking | 1.0000 | 0.0000 |
| Bad Picking | 0.6154 | 0.3846 |
