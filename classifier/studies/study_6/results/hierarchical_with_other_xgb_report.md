# Hierarchical Architecture With Other - XGBoost

## Combined Performance

**Accuracy:** 0.6641

**Macro F1:** 0.6841

**Weighted F1:** 0.6604

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.8788 | 0.6591 | 0.7532 | 44 |
| Idle | 0.4924 | 0.9559 | 0.6500 | 68 |
| Good Picking | 0.9535 | 0.4100 | 0.5734 | 100 |
| Bad Picking | 0.4434 | 0.4563 | 0.4498 | 103 |
| Pushing | 0.9878 | 1.0000 | 0.9939 | 81 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 29 | 11 | 2 | 2 | 0 |
| Idle | 1 | 65 | 0 | 2 | 0 |
| Good Picking | 2 | 1 | 41 | 55 | 1 |
| Bad Picking | 1 | 55 | 0 | 47 | 0 |
| Pushing | 0 | 0 | 0 | 0 | 81 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.6591 | 0.2500 | 0.0455 | 0.0455 | 0.0000 |
| Idle | 0.0147 | 0.9559 | 0.0000 | 0.0294 | 0.0000 |
| Good Picking | 0.0200 | 0.0100 | 0.4100 | 0.5500 | 0.0100 |
| Bad Picking | 0.0097 | 0.5340 | 0.0000 | 0.4563 | 0.0000 |
| Pushing | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |

## Stage 1 — Activity Classification

**Accuracy:** 0.8258

**Macro F1:** 0.8173

**Weighted F1:** 0.8348

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.9032 | 0.6364 | 0.7467 | 44 |
| Idle | 0.5328 | 0.9559 | 0.6842 | 68 |
| Picking | 0.9444 | 0.7537 | 0.8384 | 203 |
| Pushing | 1.0000 | 1.0000 | 1.0000 | 81 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Picking | Pushing |
|---|---:|---:|---:|---:|
| Bending | 28 | 10 | 6 | 0 |
| Idle | 0 | 65 | 3 | 0 |
| Picking | 3 | 47 | 153 | 0 |
| Pushing | 0 | 0 | 0 | 81 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Picking | Pushing |
|---|---:|---:|---:|---:|
| Bending | 0.6364 | 0.2273 | 0.1364 | 0.0000 |
| Idle | 0.0000 | 0.9559 | 0.0441 | 0.0000 |
| Picking | 0.0148 | 0.2315 | 0.7537 | 0.0000 |
| Pushing | 0.0000 | 0.0000 | 0.0000 | 1.0000 |

## Stage 2 — Picking Classification

**Accuracy:** 0.6970

**Macro F1:** 0.6275

**Weighted F1:** 0.6789

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Good Picking | 0.9535 | 0.4100 | 0.5734 | 100 |
| Bad Picking | 0.4486 | 0.4660 | 0.4571 | 103 |
| Other | 0.7602 | 0.9689 | 0.8519 | 193 |

### Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking | Other |
|---|---:|---:|---:|
| Good Picking | 41 | 55 | 4 |
| Bad Picking | 0 | 48 | 55 |
| Other | 2 | 4 | 187 |

### Normalized Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking | Other |
|---|---:|---:|---:|
| Good Picking | 0.4100 | 0.5500 | 0.0400 |
| Bad Picking | 0.0000 | 0.4660 | 0.5340 |
| Other | 0.0104 | 0.0207 | 0.9689 |
