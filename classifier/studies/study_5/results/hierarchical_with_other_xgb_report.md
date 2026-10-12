# Hierarchical Architecture With Other - XGBoost

## Combined Performance

**Accuracy:** 0.6426

**Macro F1:** 0.6656

**Weighted F1:** 0.6342

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.8716 | 0.7090 | 0.7819 | 134 |
| Idle | 0.4748 | 0.9706 | 0.6377 | 204 |
| Good Picking | 0.8976 | 0.3787 | 0.5327 | 301 |
| Bad Picking | 0.3973 | 0.3754 | 0.3860 | 309 |
| Pushing | 0.9838 | 0.9959 | 0.9898 | 244 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 95 | 31 | 6 | 1 | 1 |
| Idle | 3 | 198 | 0 | 3 | 0 |
| Good Picking | 7 | 7 | 114 | 172 | 1 |
| Bad Picking | 3 | 181 | 7 | 116 | 2 |
| Pushing | 1 | 0 | 0 | 0 | 243 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.7090 | 0.2313 | 0.0448 | 0.0075 | 0.0075 |
| Idle | 0.0147 | 0.9706 | 0.0000 | 0.0147 | 0.0000 |
| Good Picking | 0.0233 | 0.0233 | 0.3787 | 0.5714 | 0.0033 |
| Bad Picking | 0.0097 | 0.5858 | 0.0227 | 0.3754 | 0.0065 |
| Pushing | 0.0041 | 0.0000 | 0.0000 | 0.0000 | 0.9959 |

## Stage 1 — Activity Classification

**Accuracy:** 0.8180

**Macro F1:** 0.8185

**Weighted F1:** 0.8302

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.8952 | 0.7015 | 0.7866 | 134 |
| Idle | 0.5065 | 0.9608 | 0.6633 | 204 |
| Picking | 0.9714 | 0.7246 | 0.8300 | 610 |
| Pushing | 0.9918 | 0.9959 | 0.9939 | 244 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Picking | Pushing |
|---|---:|---:|---:|---:|
| Bending | 94 | 31 | 8 | 1 |
| Idle | 3 | 196 | 5 | 0 |
| Picking | 7 | 160 | 442 | 1 |
| Pushing | 1 | 0 | 0 | 243 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Picking | Pushing |
|---|---:|---:|---:|---:|
| Bending | 0.7015 | 0.2313 | 0.0597 | 0.0075 |
| Idle | 0.0147 | 0.9608 | 0.0245 | 0.0000 |
| Picking | 0.0115 | 0.2623 | 0.7246 | 0.0016 |
| Pushing | 0.0041 | 0.0000 | 0.0000 | 0.9959 |

## Stage 2 — Picking Classification

**Accuracy:** 0.6762

**Macro F1:** 0.5932

**Weighted F1:** 0.6516

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Good Picking | 0.8976 | 0.3787 | 0.5327 | 301 |
| Bad Picking | 0.4067 | 0.3948 | 0.4007 | 309 |
| Other | 0.7451 | 0.9794 | 0.8463 | 582 |

### Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking | Other |
|---|---:|---:|---:|
| Good Picking | 114 | 172 | 15 |
| Bad Picking | 7 | 122 | 180 |
| Other | 6 | 6 | 570 |

### Normalized Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking | Other |
|---|---:|---:|---:|
| Good Picking | 0.3787 | 0.5714 | 0.0498 |
| Bad Picking | 0.0227 | 0.3948 | 0.5825 |
| Other | 0.0103 | 0.0103 | 0.9794 |
