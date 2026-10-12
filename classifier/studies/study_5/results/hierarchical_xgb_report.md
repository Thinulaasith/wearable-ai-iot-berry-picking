# Standard Hierarchical Architecture - XGBoost

## Combined Performance

**Accuracy:** 0.6678

**Macro F1:** 0.6899

**Weighted F1:** 0.6624

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.8952 | 0.7015 | 0.7866 | 134 |
| Idle | 0.5065 | 0.9608 | 0.6633 | 204 |
| Good Picking | 0.9084 | 0.3953 | 0.5509 | 301 |
| Bad Picking | 0.4444 | 0.4660 | 0.4550 | 309 |
| Pushing | 0.9918 | 0.9959 | 0.9939 | 244 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 94 | 31 | 6 | 2 | 1 |
| Idle | 3 | 196 | 0 | 5 | 0 |
| Good Picking | 5 | 4 | 119 | 173 | 0 |
| Bad Picking | 2 | 156 | 6 | 144 | 1 |
| Pushing | 1 | 0 | 0 | 0 | 243 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.7015 | 0.2313 | 0.0448 | 0.0149 | 0.0075 |
| Idle | 0.0147 | 0.9608 | 0.0000 | 0.0245 | 0.0000 |
| Good Picking | 0.0166 | 0.0133 | 0.3953 | 0.5748 | 0.0000 |
| Bad Picking | 0.0065 | 0.5049 | 0.0194 | 0.4660 | 0.0032 |
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

**Accuracy:** 0.6951

**Macro F1:** 0.6653

**Weighted F1:** 0.6666

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Good Picking | 0.9528 | 0.4020 | 0.5654 | 301 |
| Bad Picking | 0.6273 | 0.9806 | 0.7652 | 309 |

### Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking |
|---|---:|---:|
| Good Picking | 121 | 180 |
| Bad Picking | 6 | 303 |

### Normalized Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking |
|---|---:|---:|
| Good Picking | 0.4020 | 0.5980 |
| Bad Picking | 0.0194 | 0.9806 |
