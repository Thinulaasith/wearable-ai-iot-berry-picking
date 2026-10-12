# Hierarchical Architecture With Other - Random Forest

## Combined Performance

**Accuracy:** 0.8559

**Macro F1:** 0.7857

**Weighted F1:** 0.8474

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.6897 | 0.5405 | 0.6061 | 37 |
| Idle | 0.7886 | 0.9510 | 0.8622 | 102 |
| Good Picking | 0.7442 | 0.8889 | 0.8101 | 36 |
| Bad Picking | 0.8667 | 0.5200 | 0.6500 | 50 |
| Pushing | 1.0000 | 1.0000 | 1.0000 | 122 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 20 | 15 | 2 | 0 | 0 |
| Idle | 1 | 97 | 0 | 4 | 0 |
| Good Picking | 4 | 0 | 32 | 0 | 0 |
| Bad Picking | 4 | 11 | 9 | 26 | 0 |
| Pushing | 0 | 0 | 0 | 0 | 122 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.5405 | 0.4054 | 0.0541 | 0.0000 | 0.0000 |
| Idle | 0.0098 | 0.9510 | 0.0000 | 0.0392 | 0.0000 |
| Good Picking | 0.1111 | 0.0000 | 0.8889 | 0.0000 | 0.0000 |
| Bad Picking | 0.0800 | 0.2200 | 0.1800 | 0.5200 | 0.0000 |
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

**Accuracy:** 0.9020

**Macro F1:** 0.8073

**Weighted F1:** 0.8958

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Good Picking | 0.7442 | 0.8889 | 0.8101 | 36 |
| Bad Picking | 0.8438 | 0.5400 | 0.6585 | 50 |
| Other | 0.9338 | 0.9732 | 0.9531 | 261 |

### Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking | Other |
|---|---:|---:|---:|
| Good Picking | 32 | 0 | 4 |
| Bad Picking | 9 | 27 | 14 |
| Other | 2 | 5 | 254 |

### Normalized Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking | Other |
|---|---:|---:|---:|
| Good Picking | 0.8889 | 0.0000 | 0.1111 |
| Bad Picking | 0.1800 | 0.5400 | 0.2800 |
| Other | 0.0077 | 0.0192 | 0.9732 |
