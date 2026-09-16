# Standard Hierarchical Architecture - Random Forest

## Combined Performance

**Accuracy:** 0.8460

**Macro F1:** 0.7742

**Weighted F1:** 0.8352

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.8511 | 0.5333 | 0.6557 | 75 |
| Idle | 0.7751 | 0.9461 | 0.8521 | 204 |
| Good Picking | 0.7033 | 0.8889 | 0.7853 | 72 |
| Bad Picking | 0.7705 | 0.4700 | 0.5839 | 100 |
| Pushing | 0.9879 | 1.0000 | 0.9939 | 244 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 40 | 30 | 1 | 3 | 1 |
| Idle | 1 | 193 | 0 | 9 | 1 |
| Good Picking | 4 | 1 | 64 | 2 | 1 |
| Bad Picking | 2 | 25 | 26 | 47 | 0 |
| Pushing | 0 | 0 | 0 | 0 | 244 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.5333 | 0.4000 | 0.0133 | 0.0400 | 0.0133 |
| Idle | 0.0049 | 0.9461 | 0.0000 | 0.0441 | 0.0049 |
| Good Picking | 0.0556 | 0.0139 | 0.8889 | 0.0278 | 0.0139 |
| Bad Picking | 0.0200 | 0.2500 | 0.2600 | 0.4700 | 0.0000 |
| Pushing | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |

## Stage 1 — Activity Classification

**Accuracy:** 0.8863

**Macro F1:** 0.8399

**Weighted F1:** 0.8822

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.8511 | 0.5333 | 0.6557 | 75 |
| Idle | 0.7751 | 0.9461 | 0.8521 | 204 |
| Picking | 0.9145 | 0.8081 | 0.8580 | 172 |
| Pushing | 0.9879 | 1.0000 | 0.9939 | 244 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Picking | Pushing |
|---|---:|---:|---:|---:|
| Bending | 40 | 30 | 4 | 1 |
| Idle | 1 | 193 | 9 | 1 |
| Picking | 6 | 26 | 139 | 1 |
| Pushing | 0 | 0 | 0 | 244 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Picking | Pushing |
|---|---:|---:|---:|---:|
| Bending | 0.5333 | 0.4000 | 0.0533 | 0.0133 |
| Idle | 0.0049 | 0.9461 | 0.0441 | 0.0049 |
| Picking | 0.0349 | 0.1512 | 0.8081 | 0.0058 |
| Pushing | 0.0000 | 0.0000 | 0.0000 | 1.0000 |

## Stage 2 — Picking Classification

**Accuracy:** 0.8198

**Macro F1:** 0.8197

**Weighted F1:** 0.8202

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Good Picking | 0.7113 | 0.9583 | 0.8166 | 72 |
| Bad Picking | 0.9600 | 0.7200 | 0.8229 | 100 |

### Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking |
|---|---:|---:|
| Good Picking | 69 | 3 |
| Bad Picking | 28 | 72 |

### Normalized Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking |
|---|---:|---:|
| Good Picking | 0.9583 | 0.0417 |
| Bad Picking | 0.2800 | 0.7200 |
