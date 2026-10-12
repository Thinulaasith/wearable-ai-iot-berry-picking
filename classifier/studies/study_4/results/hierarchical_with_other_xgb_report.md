# Hierarchical Architecture With Other - XGBoost

## Combined Performance

**Accuracy:** 0.6336

**Macro F1:** 0.6604

**Weighted F1:** 0.6284

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.8889 | 0.7164 | 0.7934 | 67 |
| Idle | 0.4545 | 0.9314 | 0.6109 | 102 |
| Good Picking | 0.9661 | 0.3800 | 0.5455 | 150 |
| Bad Picking | 0.3716 | 0.3571 | 0.3642 | 154 |
| Pushing | 0.9760 | 1.0000 | 0.9879 | 122 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 48 | 16 | 2 | 1 | 0 |
| Idle | 1 | 95 | 0 | 6 | 0 |
| Good Picking | 3 | 2 | 57 | 86 | 2 |
| Bad Picking | 2 | 96 | 0 | 55 | 1 |
| Pushing | 0 | 0 | 0 | 0 | 122 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.7164 | 0.2388 | 0.0299 | 0.0149 | 0.0000 |
| Idle | 0.0098 | 0.9314 | 0.0000 | 0.0588 | 0.0000 |
| Good Picking | 0.0200 | 0.0133 | 0.3800 | 0.5733 | 0.0133 |
| Bad Picking | 0.0130 | 0.6234 | 0.0000 | 0.3571 | 0.0065 |
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

**Accuracy:** 0.6622

**Macro F1:** 0.5819

**Weighted F1:** 0.6392

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Good Picking | 0.9667 | 0.3867 | 0.5524 | 150 |
| Bad Picking | 0.3691 | 0.3571 | 0.3630 | 154 |
| Other | 0.7280 | 0.9656 | 0.8301 | 291 |

### Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking | Other |
|---|---:|---:|---:|
| Good Picking | 58 | 86 | 6 |
| Bad Picking | 0 | 55 | 99 |
| Other | 2 | 8 | 281 |

### Normalized Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking | Other |
|---|---:|---:|---:|
| Good Picking | 0.3867 | 0.5733 | 0.0400 |
| Bad Picking | 0.0000 | 0.3571 | 0.6429 |
| Other | 0.0069 | 0.0275 | 0.9656 |
