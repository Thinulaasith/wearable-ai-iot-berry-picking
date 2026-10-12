# Standard Hierarchical Architecture - Random Forest

## Combined Performance

**Accuracy:** 0.8952

**Macro F1:** 0.7762

**Weighted F1:** 0.8895

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.7647 | 0.6842 | 0.7222 | 19 |
| Idle | 0.9084 | 0.9754 | 0.9407 | 122 |
| Good Picking | 0.5000 | 0.7500 | 0.6000 | 12 |
| Bad Picking | 0.8065 | 0.5208 | 0.6329 | 48 |
| Pushing | 0.9708 | 1.0000 | 0.9852 | 133 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 13 | 2 | 1 | 0 | 3 |
| Idle | 0 | 119 | 0 | 3 | 0 |
| Good Picking | 0 | 0 | 9 | 3 | 0 |
| Bad Picking | 4 | 10 | 8 | 25 | 1 |
| Pushing | 0 | 0 | 0 | 0 | 133 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.6842 | 0.1053 | 0.0526 | 0.0000 | 0.1579 |
| Idle | 0.0000 | 0.9754 | 0.0000 | 0.0246 | 0.0000 |
| Good Picking | 0.0000 | 0.0000 | 0.7500 | 0.2500 | 0.0000 |
| Bad Picking | 0.0833 | 0.2083 | 0.1667 | 0.5208 | 0.0208 |
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

**Accuracy:** 0.7667

**Macro F1:** 0.7017

**Weighted F1:** 0.7852

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Good Picking | 0.4500 | 0.7500 | 0.5625 | 12 |
| Bad Picking | 0.9250 | 0.7708 | 0.8409 | 48 |

### Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking |
|---|---:|---:|
| Good Picking | 9 | 3 |
| Bad Picking | 11 | 37 |

### Normalized Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking |
|---|---:|---:|
| Good Picking | 0.7500 | 0.2500 |
| Bad Picking | 0.2292 | 0.7708 |
