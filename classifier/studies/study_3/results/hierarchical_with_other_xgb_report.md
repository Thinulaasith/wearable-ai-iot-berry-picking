# Hierarchical Architecture With Other - XGBoost

## Combined Performance

**Accuracy:** 0.8417

**Macro F1:** 0.7717

**Weighted F1:** 0.8307

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.8077 | 0.5600 | 0.6614 | 75 |
| Idle | 0.7529 | 0.9412 | 0.8366 | 204 |
| Good Picking | 0.7294 | 0.8611 | 0.7898 | 72 |
| Bad Picking | 0.8036 | 0.4500 | 0.5769 | 100 |
| Pushing | 0.9879 | 1.0000 | 0.9939 | 244 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 42 | 31 | 2 | 0 | 0 |
| Idle | 3 | 192 | 0 | 9 | 0 |
| Good Picking | 3 | 2 | 62 | 2 | 3 |
| Bad Picking | 4 | 30 | 21 | 45 | 0 |
| Pushing | 0 | 0 | 0 | 0 | 244 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.5600 | 0.4133 | 0.0267 | 0.0000 | 0.0000 |
| Idle | 0.0147 | 0.9412 | 0.0000 | 0.0441 | 0.0000 |
| Good Picking | 0.0417 | 0.0278 | 0.8611 | 0.0278 | 0.0417 |
| Bad Picking | 0.0400 | 0.3000 | 0.2100 | 0.4500 | 0.0000 |
| Pushing | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |

## Stage 1 — Activity Classification

**Accuracy:** 0.8849

**Macro F1:** 0.8420

**Weighted F1:** 0.8813

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.8723 | 0.5467 | 0.6721 | 75 |
| Idle | 0.7782 | 0.9118 | 0.8397 | 204 |
| Picking | 0.8889 | 0.8372 | 0.8623 | 172 |
| Pushing | 0.9879 | 1.0000 | 0.9939 | 244 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Picking | Pushing |
|---|---:|---:|---:|---:|
| Bending | 41 | 31 | 3 | 0 |
| Idle | 3 | 186 | 15 | 0 |
| Picking | 3 | 22 | 144 | 3 |
| Pushing | 0 | 0 | 0 | 244 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Picking | Pushing |
|---|---:|---:|---:|---:|
| Bending | 0.5467 | 0.4133 | 0.0400 | 0.0000 |
| Idle | 0.0147 | 0.9118 | 0.0735 | 0.0000 |
| Picking | 0.0174 | 0.1279 | 0.8372 | 0.0174 |
| Pushing | 0.0000 | 0.0000 | 0.0000 | 1.0000 |

## Stage 2 — Picking Classification

**Accuracy:** 0.8878

**Macro F1:** 0.7712

**Weighted F1:** 0.8785

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Good Picking | 0.7294 | 0.8611 | 0.7898 | 72 |
| Bad Picking | 0.7667 | 0.4600 | 0.5750 | 100 |
| Other | 0.9255 | 0.9732 | 0.9487 | 523 |

### Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking | Other |
|---|---:|---:|---:|
| Good Picking | 62 | 2 | 8 |
| Bad Picking | 21 | 46 | 33 |
| Other | 2 | 12 | 509 |

### Normalized Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking | Other |
|---|---:|---:|---:|
| Good Picking | 0.8611 | 0.0278 | 0.1111 |
| Bad Picking | 0.2100 | 0.4600 | 0.3300 |
| Other | 0.0038 | 0.0229 | 0.9732 |
