# Standard Hierarchical Architecture - XGBoost

## Combined Performance

**Accuracy:** 0.8432

**Macro F1:** 0.7773

**Weighted F1:** 0.8350

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.8367 | 0.5467 | 0.6613 | 75 |
| Idle | 0.7782 | 0.9118 | 0.8397 | 204 |
| Good Picking | 0.7191 | 0.8889 | 0.7950 | 72 |
| Bad Picking | 0.7183 | 0.5100 | 0.5965 | 100 |
| Pushing | 0.9879 | 1.0000 | 0.9939 | 244 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 41 | 31 | 1 | 2 | 0 |
| Idle | 3 | 186 | 0 | 15 | 0 |
| Good Picking | 2 | 0 | 64 | 3 | 3 |
| Bad Picking | 3 | 22 | 24 | 51 | 0 |
| Pushing | 0 | 0 | 0 | 0 | 244 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.5467 | 0.4133 | 0.0133 | 0.0267 | 0.0000 |
| Idle | 0.0147 | 0.9118 | 0.0000 | 0.0735 | 0.0000 |
| Good Picking | 0.0278 | 0.0000 | 0.8889 | 0.0417 | 0.0417 |
| Bad Picking | 0.0300 | 0.2200 | 0.2400 | 0.5100 | 0.0000 |
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

**Accuracy:** 0.8372

**Macro F1:** 0.8369

**Weighted F1:** 0.8381

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Good Picking | 0.7391 | 0.9444 | 0.8293 | 72 |
| Bad Picking | 0.9500 | 0.7600 | 0.8444 | 100 |

### Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking |
|---|---:|---:|
| Good Picking | 68 | 4 |
| Bad Picking | 24 | 76 |

### Normalized Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking |
|---|---:|---:|
| Good Picking | 0.9444 | 0.0556 |
| Bad Picking | 0.2400 | 0.7600 |
