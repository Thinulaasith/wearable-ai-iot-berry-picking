# Hierarchical Architecture With Other - Random Forest

## Combined Performance

**Accuracy:** 0.6695

**Macro F1:** 0.6856

**Weighted F1:** 0.6653

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.8447 | 0.6493 | 0.7342 | 134 |
| Idle | 0.4963 | 0.9755 | 0.6579 | 204 |
| Good Picking | 0.9236 | 0.4419 | 0.5978 | 301 |
| Bad Picking | 0.4631 | 0.4466 | 0.4547 | 309 |
| Pushing | 0.9797 | 0.9877 | 0.9837 | 244 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 87 | 32 | 8 | 4 | 3 |
| Idle | 3 | 199 | 0 | 1 | 1 |
| Good Picking | 8 | 4 | 133 | 155 | 1 |
| Bad Picking | 3 | 165 | 3 | 138 | 0 |
| Pushing | 2 | 1 | 0 | 0 | 241 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.6493 | 0.2388 | 0.0597 | 0.0299 | 0.0224 |
| Idle | 0.0147 | 0.9755 | 0.0000 | 0.0049 | 0.0049 |
| Good Picking | 0.0266 | 0.0133 | 0.4419 | 0.5150 | 0.0033 |
| Bad Picking | 0.0097 | 0.5340 | 0.0097 | 0.4466 | 0.0000 |
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

**Accuracy:** 0.7039

**Macro F1:** 0.6349

**Weighted F1:** 0.6852

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Good Picking | 0.9172 | 0.4419 | 0.5964 | 301 |
| Bad Picking | 0.4631 | 0.4466 | 0.4547 | 309 |
| Other | 0.7583 | 0.9759 | 0.8535 | 582 |

### Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking | Other |
|---|---:|---:|---:|
| Good Picking | 133 | 155 | 13 |
| Bad Picking | 3 | 138 | 168 |
| Other | 9 | 5 | 568 |

### Normalized Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking | Other |
|---|---:|---:|---:|
| Good Picking | 0.4419 | 0.5150 | 0.0432 |
| Bad Picking | 0.0097 | 0.4466 | 0.5437 |
| Other | 0.0155 | 0.0086 | 0.9759 |
