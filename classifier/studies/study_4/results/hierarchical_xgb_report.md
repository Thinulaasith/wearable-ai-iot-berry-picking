# Standard Hierarchical Architecture - XGBoost

## Combined Performance

**Accuracy:** 0.6471

**Macro F1:** 0.6714

**Weighted F1:** 0.6427

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.9020 | 0.6866 | 0.7797 | 67 |
| Idle | 0.4821 | 0.9216 | 0.6330 | 102 |
| Good Picking | 0.9483 | 0.3667 | 0.5288 | 150 |
| Bad Picking | 0.4072 | 0.4416 | 0.4237 | 154 |
| Pushing | 0.9839 | 1.0000 | 0.9919 | 122 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 46 | 16 | 2 | 3 | 0 |
| Idle | 1 | 94 | 0 | 7 | 0 |
| Good Picking | 2 | 2 | 55 | 89 | 2 |
| Bad Picking | 2 | 83 | 1 | 68 | 0 |
| Pushing | 0 | 0 | 0 | 0 | 122 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.6866 | 0.2388 | 0.0299 | 0.0448 | 0.0000 |
| Idle | 0.0098 | 0.9216 | 0.0000 | 0.0686 | 0.0000 |
| Good Picking | 0.0133 | 0.0133 | 0.3667 | 0.5933 | 0.0133 |
| Bad Picking | 0.0130 | 0.5390 | 0.0065 | 0.4416 | 0.0000 |
| Pushing | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |

## Stage 1 — Activity Classification

**Accuracy:** 0.7983

**Macro F1:** 0.8025

**Weighted F1:** 0.8111

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.9020 | 0.6866 | 0.7797 | 67 |
| Idle | 0.4821 | 0.9216 | 0.6330 | 102 |
| Picking | 0.9467 | 0.7007 | 0.8053 | 304 |
| Pushing | 0.9839 | 1.0000 | 0.9919 | 122 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Picking | Pushing |
|---|---:|---:|---:|---:|
| Bending | 46 | 16 | 5 | 0 |
| Idle | 1 | 94 | 7 | 0 |
| Picking | 4 | 85 | 213 | 2 |
| Pushing | 0 | 0 | 0 | 122 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Picking | Pushing |
|---|---:|---:|---:|---:|
| Bending | 0.6866 | 0.2388 | 0.0746 | 0.0000 |
| Idle | 0.0098 | 0.9216 | 0.0686 | 0.0000 |
| Picking | 0.0132 | 0.2796 | 0.7007 | 0.0066 |
| Pushing | 0.0000 | 0.0000 | 0.0000 | 1.0000 |

## Stage 2 — Picking Classification

**Accuracy:** 0.6908

**Macro F1:** 0.6565

**Weighted F1:** 0.6580

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Good Picking | 0.9828 | 0.3800 | 0.5481 | 150 |
| Bad Picking | 0.6220 | 0.9935 | 0.7650 | 154 |

### Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking |
|---|---:|---:|
| Good Picking | 57 | 93 |
| Bad Picking | 1 | 153 |

### Normalized Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking |
|---|---:|---:|
| Good Picking | 0.3800 | 0.6200 |
| Bad Picking | 0.0065 | 0.9935 |
