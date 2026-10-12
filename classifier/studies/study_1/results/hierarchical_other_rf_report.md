# Hierarchical Architecture With Other - Random Forest

## Combined Performance

**Accuracy:** 0.8802

**Macro F1:** 0.7545

**Weighted F1:** 0.8683

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.6087 | 0.7368 | 0.6667 | 19 |
| Idle | 0.8815 | 0.9754 | 0.9261 | 122 |
| Good Picking | 0.6000 | 0.7500 | 0.6667 | 12 |
| Bad Picking | 0.7917 | 0.3958 | 0.5278 | 48 |
| Pushing | 0.9708 | 1.0000 | 0.9852 | 133 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 14 | 2 | 0 | 0 | 3 |
| Idle | 0 | 119 | 0 | 3 | 0 |
| Good Picking | 0 | 1 | 9 | 2 | 0 |
| Bad Picking | 9 | 13 | 6 | 19 | 1 |
| Pushing | 0 | 0 | 0 | 0 | 133 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.7368 | 0.1053 | 0.0000 | 0.0000 | 0.1579 |
| Idle | 0.0000 | 0.9754 | 0.0000 | 0.0246 | 0.0000 |
| Good Picking | 0.0000 | 0.0833 | 0.7500 | 0.1667 | 0.0000 |
| Bad Picking | 0.1875 | 0.2708 | 0.1250 | 0.3958 | 0.0208 |
| Pushing | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |

## Stage 1 — Activity Classification

**Accuracy:** 0.9281

**Macro F1:** 0.8685

**Weighted F1:** 0.9253

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.7647 | 0.6842 | 0.7222 | 19 |
| Idle | 0.9084 | 0.9754 | 0.9407 | 122 |
| Picking | 0.9184 | 0.7500 | 0.8257 | 60 |
| Pushing | 0.9708 | 1.0000 | 0.9852 | 133 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Picking | Pushing |
|---|---:|---:|---:|---:|
| Bending | 13 | 2 | 1 | 3 |
| Idle | 0 | 119 | 3 | 0 |
| Picking | 4 | 10 | 45 | 1 |
| Pushing | 0 | 0 | 0 | 133 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Picking | Pushing |
|---|---:|---:|---:|---:|
| Bending | 0.6842 | 0.1053 | 0.0526 | 0.1579 |
| Idle | 0.0000 | 0.9754 | 0.0246 | 0.0000 |
| Picking | 0.0667 | 0.1667 | 0.7500 | 0.0167 |
| Pushing | 0.0000 | 0.0000 | 0.0000 | 1.0000 |

## Stage 2 — Picking Classification

**Accuracy:** 0.8892

**Macro F1:** 0.7097

**Weighted F1:** 0.8762

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Good Picking | 0.6000 | 0.7500 | 0.6667 | 12 |
| Bad Picking | 0.7308 | 0.3958 | 0.5135 | 48 |
| Other | 0.9181 | 0.9818 | 0.9489 | 274 |

### Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking | Other |
|---|---:|---:|---:|
| Good Picking | 9 | 2 | 1 |
| Bad Picking | 6 | 19 | 23 |
| Other | 0 | 5 | 269 |

### Normalized Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking | Other |
|---|---:|---:|---:|
| Good Picking | 0.7500 | 0.1667 | 0.0833 |
| Bad Picking | 0.1250 | 0.3958 | 0.4792 |
| Other | 0.0000 | 0.0182 | 0.9818 |
