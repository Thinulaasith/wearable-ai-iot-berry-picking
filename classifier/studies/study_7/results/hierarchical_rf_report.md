# Standard Hierarchical Architecture - Random Forest

## Combined Performance

**Accuracy:** 0.8530

**Macro F1:** 0.7843

**Weighted F1:** 0.8455

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.7407 | 0.5405 | 0.6250 | 37 |
| Idle | 0.7917 | 0.9314 | 0.8559 | 102 |
| Good Picking | 0.7111 | 0.8889 | 0.7901 | 36 |
| Bad Picking | 0.8182 | 0.5400 | 0.6506 | 50 |
| Pushing | 1.0000 | 1.0000 | 1.0000 | 122 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 20 | 15 | 2 | 0 | 0 |
| Idle | 1 | 95 | 0 | 6 | 0 |
| Good Picking | 4 | 0 | 32 | 0 | 0 |
| Bad Picking | 2 | 10 | 11 | 27 | 0 |
| Pushing | 0 | 0 | 0 | 0 | 122 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.5405 | 0.4054 | 0.0541 | 0.0000 | 0.0000 |
| Idle | 0.0098 | 0.9314 | 0.0000 | 0.0588 | 0.0000 |
| Good Picking | 0.1111 | 0.0000 | 0.8889 | 0.0000 | 0.0000 |
| Bad Picking | 0.0400 | 0.2000 | 0.2200 | 0.5400 | 0.0000 |
| Pushing | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |

## Stage 1 — Activity Classification

**Accuracy:** 0.8847

**Macro F1:** 0.8336

**Weighted F1:** 0.8814

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.7407 | 0.5405 | 0.6250 | 37 |
| Idle | 0.7917 | 0.9314 | 0.8559 | 102 |
| Picking | 0.8974 | 0.8140 | 0.8537 | 86 |
| Pushing | 1.0000 | 1.0000 | 1.0000 | 122 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Picking | Pushing |
|---|---:|---:|---:|---:|
| Bending | 20 | 15 | 2 | 0 |
| Idle | 1 | 95 | 6 | 0 |
| Picking | 6 | 10 | 70 | 0 |
| Pushing | 0 | 0 | 0 | 122 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Picking | Pushing |
|---|---:|---:|---:|---:|
| Bending | 0.5405 | 0.4054 | 0.0541 | 0.0000 |
| Idle | 0.0098 | 0.9314 | 0.0588 | 0.0000 |
| Picking | 0.0698 | 0.1163 | 0.8140 | 0.0000 |
| Pushing | 0.0000 | 0.0000 | 0.0000 | 1.0000 |

## Stage 2 — Picking Classification

**Accuracy:** 0.8721

**Macro F1:** 0.8719

**Weighted F1:** 0.8727

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Good Picking | 0.7660 | 1.0000 | 0.8675 | 36 |
| Bad Picking | 1.0000 | 0.7800 | 0.8764 | 50 |

### Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking |
|---|---:|---:|
| Good Picking | 36 | 0 |
| Bad Picking | 11 | 39 |

### Normalized Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking |
|---|---:|---:|
| Good Picking | 1.0000 | 0.0000 |
| Bad Picking | 0.2200 | 0.7800 |
