# Standard Hierarchical Architecture - XGBoost

## Combined Performance

**Accuracy:** 0.6717

**Macro F1:** 0.6892

**Weighted F1:** 0.6651

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.9032 | 0.6364 | 0.7467 | 44 |
| Idle | 0.5328 | 0.9559 | 0.6842 | 68 |
| Good Picking | 0.9474 | 0.3600 | 0.5217 | 100 |
| Bad Picking | 0.4516 | 0.5437 | 0.4934 | 103 |
| Pushing | 1.0000 | 1.0000 | 1.0000 | 81 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 28 | 10 | 2 | 4 | 0 |
| Idle | 0 | 65 | 0 | 3 | 0 |
| Good Picking | 2 | 1 | 36 | 61 | 0 |
| Bad Picking | 1 | 46 | 0 | 56 | 0 |
| Pushing | 0 | 0 | 0 | 0 | 81 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.6364 | 0.2273 | 0.0455 | 0.0909 | 0.0000 |
| Idle | 0.0000 | 0.9559 | 0.0000 | 0.0441 | 0.0000 |
| Good Picking | 0.0200 | 0.0100 | 0.3600 | 0.6100 | 0.0000 |
| Bad Picking | 0.0097 | 0.4466 | 0.0000 | 0.5437 | 0.0000 |
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

**Accuracy:** 0.6897

**Macro F1:** 0.6530

**Weighted F1:** 0.6546

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Good Picking | 1.0000 | 0.3700 | 0.5401 | 100 |
| Bad Picking | 0.6205 | 1.0000 | 0.7658 | 103 |

### Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking |
|---|---:|---:|
| Good Picking | 37 | 63 |
| Bad Picking | 0 | 103 |

### Normalized Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking |
|---|---:|---:|
| Good Picking | 0.3700 | 0.6300 |
| Bad Picking | 0.0000 | 1.0000 |
