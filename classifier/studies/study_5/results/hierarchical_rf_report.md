# Standard Hierarchical Architecture - Random Forest

## Combined Performance

**Accuracy:** 0.6896

**Macro F1:** 0.7029

**Weighted F1:** 0.6865

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.9000 | 0.6045 | 0.7232 | 134 |
| Idle | 0.5387 | 0.9559 | 0.6890 | 204 |
| Good Picking | 0.8831 | 0.4518 | 0.5978 | 301 |
| Bad Picking | 0.4971 | 0.5469 | 0.5208 | 309 |
| Pushing | 0.9797 | 0.9877 | 0.9837 | 244 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 81 | 30 | 14 | 6 | 3 |
| Idle | 2 | 195 | 0 | 6 | 1 |
| Good Picking | 4 | 1 | 136 | 159 | 1 |
| Bad Picking | 1 | 135 | 4 | 169 | 0 |
| Pushing | 2 | 1 | 0 | 0 | 241 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.6045 | 0.2239 | 0.1045 | 0.0448 | 0.0224 |
| Idle | 0.0098 | 0.9559 | 0.0000 | 0.0294 | 0.0049 |
| Good Picking | 0.0133 | 0.0033 | 0.4518 | 0.5282 | 0.0033 |
| Bad Picking | 0.0032 | 0.4369 | 0.0129 | 0.5469 | 0.0000 |
| Pushing | 0.0082 | 0.0041 | 0.0000 | 0.0000 | 0.9877 |

## Stage 1 — Activity Classification

**Accuracy:** 0.8263

**Macro F1:** 0.8109

**Weighted F1:** 0.8345

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.9000 | 0.6045 | 0.7232 | 134 |
| Idle | 0.5387 | 0.9559 | 0.6890 | 204 |
| Picking | 0.9474 | 0.7672 | 0.8478 | 610 |
| Pushing | 0.9797 | 0.9877 | 0.9837 | 244 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Picking | Pushing |
|---|---:|---:|---:|---:|
| Bending | 81 | 30 | 20 | 3 |
| Idle | 2 | 195 | 6 | 1 |
| Picking | 5 | 136 | 468 | 1 |
| Pushing | 2 | 1 | 0 | 241 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Picking | Pushing |
|---|---:|---:|---:|---:|
| Bending | 0.6045 | 0.2239 | 0.1493 | 0.0224 |
| Idle | 0.0098 | 0.9559 | 0.0294 | 0.0049 |
| Picking | 0.0082 | 0.2230 | 0.7672 | 0.0016 |
| Pushing | 0.0082 | 0.0041 | 0.0000 | 0.9877 |

## Stage 2 — Picking Classification

**Accuracy:** 0.7230

**Macro F1:** 0.6999

**Weighted F1:** 0.7010

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Good Picking | 0.9714 | 0.4518 | 0.6168 | 301 |
| Bad Picking | 0.6489 | 0.9871 | 0.7831 | 309 |

### Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking |
|---|---:|---:|
| Good Picking | 136 | 165 |
| Bad Picking | 4 | 305 |

### Normalized Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking |
|---|---:|---:|
| Good Picking | 0.4518 | 0.5482 |
| Bad Picking | 0.0129 | 0.9871 |
