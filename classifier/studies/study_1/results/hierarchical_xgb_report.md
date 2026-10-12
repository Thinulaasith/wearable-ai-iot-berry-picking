# Standard Hierarchical Architecture - XGBoost

## Combined Performance

**Accuracy:** 0.8772

**Macro F1:** 0.7449

**Weighted F1:** 0.8699

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.8667 | 0.6842 | 0.7647 | 19 |
| Idle | 0.8806 | 0.9672 | 0.9219 | 122 |
| Good Picking | 0.4000 | 0.6667 | 0.5000 | 12 |
| Bad Picking | 0.7500 | 0.4375 | 0.5526 | 48 |
| Pushing | 0.9708 | 1.0000 | 0.9852 | 133 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 13 | 2 | 2 | 0 | 2 |
| Idle | 0 | 118 | 0 | 4 | 0 |
| Good Picking | 0 | 1 | 8 | 3 | 0 |
| Bad Picking | 2 | 13 | 10 | 21 | 2 |
| Pushing | 0 | 0 | 0 | 0 | 133 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.6842 | 0.1053 | 0.1053 | 0.0000 | 0.1053 |
| Idle | 0.0000 | 0.9672 | 0.0000 | 0.0328 | 0.0000 |
| Good Picking | 0.0000 | 0.0833 | 0.6667 | 0.2500 | 0.0000 |
| Bad Picking | 0.0417 | 0.2708 | 0.2083 | 0.4375 | 0.0417 |
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

**Accuracy:** 0.7333

**Macro F1:** 0.6717

**Weighted F1:** 0.7570

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Good Picking | 0.4091 | 0.7500 | 0.5294 | 12 |
| Bad Picking | 0.9211 | 0.7292 | 0.8140 | 48 |

### Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking |
|---|---:|---:|
| Good Picking | 9 | 3 |
| Bad Picking | 13 | 35 |

### Normalized Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking |
|---|---:|---:|
| Good Picking | 0.7500 | 0.2500 |
| Bad Picking | 0.2708 | 0.7292 |
