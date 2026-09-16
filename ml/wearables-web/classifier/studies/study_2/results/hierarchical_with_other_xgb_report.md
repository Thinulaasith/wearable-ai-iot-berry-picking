# Hierarchical Architecture With Other - XGBoost

## Combined Performance

**Accuracy:** 0.8432

**Macro F1:** 0.7742

**Weighted F1:** 0.8325

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.8077 | 0.5600 | 0.6614 | 75 |
| Idle | 0.7559 | 0.9412 | 0.8384 | 204 |
| Good Picking | 0.7381 | 0.8611 | 0.7949 | 72 |
| Bad Picking | 0.7931 | 0.4600 | 0.5823 | 100 |
| Pushing | 0.9879 | 1.0000 | 0.9939 | 244 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 42 | 31 | 1 | 1 | 0 |
| Idle | 3 | 192 | 0 | 9 | 0 |
| Good Picking | 3 | 2 | 62 | 2 | 3 |
| Bad Picking | 4 | 29 | 21 | 46 | 0 |
| Pushing | 0 | 0 | 0 | 0 | 244 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.5600 | 0.4133 | 0.0133 | 0.0133 | 0.0000 |
| Idle | 0.0147 | 0.9412 | 0.0000 | 0.0441 | 0.0000 |
| Good Picking | 0.0417 | 0.0278 | 0.8611 | 0.0278 | 0.0417 |
| Bad Picking | 0.0400 | 0.2900 | 0.2100 | 0.4600 | 0.0000 |
| Pushing | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |

## Stage 1 — Activity Classification

**Accuracy:** 0.8820

**Macro F1:** 0.8376

**Weighted F1:** 0.8785

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.8367 | 0.5467 | 0.6613 | 75 |
| Idle | 0.7782 | 0.9118 | 0.8397 | 204 |
| Picking | 0.8875 | 0.8256 | 0.8554 | 172 |
| Pushing | 0.9879 | 1.0000 | 0.9939 | 244 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Picking | Pushing |
|---|---:|---:|---:|---:|
| Bending | 41 | 31 | 3 | 0 |
| Idle | 3 | 186 | 15 | 0 |
| Picking | 5 | 22 | 142 | 3 |
| Pushing | 0 | 0 | 0 | 244 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Picking | Pushing |
|---|---:|---:|---:|---:|
| Bending | 0.5467 | 0.4133 | 0.0400 | 0.0000 |
| Idle | 0.0147 | 0.9118 | 0.0735 | 0.0000 |
| Picking | 0.0291 | 0.1279 | 0.8256 | 0.0174 |
| Pushing | 0.0000 | 0.0000 | 0.0000 | 1.0000 |

## Stage 2 — Picking Classification

**Accuracy:** 0.8906

**Macro F1:** 0.7764

**Weighted F1:** 0.8817

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Good Picking | 0.7381 | 0.8611 | 0.7949 | 72 |
| Bad Picking | 0.7705 | 0.4700 | 0.5839 | 100 |
| Other | 0.9273 | 0.9751 | 0.9506 | 523 |

### Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking | Other |
|---|---:|---:|---:|
| Good Picking | 62 | 2 | 8 |
| Bad Picking | 21 | 47 | 32 |
| Other | 1 | 12 | 510 |

### Normalized Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking | Other |
|---|---:|---:|---:|
| Good Picking | 0.8611 | 0.0278 | 0.1111 |
| Bad Picking | 0.2100 | 0.4700 | 0.3200 |
| Other | 0.0019 | 0.0229 | 0.9751 |
