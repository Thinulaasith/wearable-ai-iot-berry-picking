# Hierarchical Architecture With Other - XGBoost

## Combined Performance

**Accuracy:** 0.8802

**Macro F1:** 0.7534

**Weighted F1:** 0.8688

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.8667 | 0.6842 | 0.7647 | 19 |
| Idle | 0.8633 | 0.9836 | 0.9195 | 122 |
| Good Picking | 0.4500 | 0.7500 | 0.5625 | 12 |
| Bad Picking | 0.8261 | 0.3958 | 0.5352 | 48 |
| Pushing | 0.9708 | 1.0000 | 0.9852 | 133 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 13 | 3 | 1 | 0 | 2 |
| Idle | 0 | 120 | 0 | 2 | 0 |
| Good Picking | 0 | 1 | 9 | 2 | 0 |
| Bad Picking | 2 | 15 | 10 | 19 | 2 |
| Pushing | 0 | 0 | 0 | 0 | 133 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.6842 | 0.1579 | 0.0526 | 0.0000 | 0.1053 |
| Idle | 0.0000 | 0.9836 | 0.0000 | 0.0164 | 0.0000 |
| Good Picking | 0.0000 | 0.0833 | 0.7500 | 0.1667 | 0.0000 |
| Bad Picking | 0.0417 | 0.3125 | 0.2083 | 0.3958 | 0.0417 |
| Pushing | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |

## Stage 1 — Activity Classification

**Accuracy:** 0.9162

**Macro F1:** 0.8624

**Weighted F1:** 0.9123

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.8667 | 0.6842 | 0.7647 | 19 |
| Idle | 0.8806 | 0.9672 | 0.9219 | 122 |
| Picking | 0.8750 | 0.7000 | 0.7778 | 60 |
| Pushing | 0.9708 | 1.0000 | 0.9852 | 133 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Picking | Pushing |
|---|---:|---:|---:|---:|
| Bending | 13 | 2 | 2 | 2 |
| Idle | 0 | 118 | 4 | 0 |
| Picking | 2 | 14 | 42 | 2 |
| Pushing | 0 | 0 | 0 | 133 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Picking | Pushing |
|---|---:|---:|---:|---:|
| Bending | 0.6842 | 0.1053 | 0.1053 | 0.1053 |
| Idle | 0.0000 | 0.9672 | 0.0328 | 0.0000 |
| Picking | 0.0333 | 0.2333 | 0.7000 | 0.0333 |
| Pushing | 0.0000 | 0.0000 | 0.0000 | 1.0000 |

## Stage 2 — Picking Classification

**Accuracy:** 0.8952

**Macro F1:** 0.6857

**Weighted F1:** 0.8841

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Good Picking | 0.4500 | 0.7500 | 0.5625 | 12 |
| Bad Picking | 0.8261 | 0.3958 | 0.5352 | 48 |
| Other | 0.9313 | 0.9891 | 0.9593 | 274 |

### Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking | Other |
|---|---:|---:|---:|
| Good Picking | 9 | 2 | 1 |
| Bad Picking | 10 | 19 | 19 |
| Other | 1 | 2 | 271 |

### Normalized Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking | Other |
|---|---:|---:|---:|
| Good Picking | 0.7500 | 0.1667 | 0.0833 |
| Bad Picking | 0.2083 | 0.3958 | 0.3958 |
| Other | 0.0036 | 0.0073 | 0.9891 |
