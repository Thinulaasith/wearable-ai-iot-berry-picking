# Hierarchical Architecture With Other - Random Forest

## Combined Performance

**Accuracy:** 0.6739

**Macro F1:** 0.6854

**Weighted F1:** 0.6691

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.8200 | 0.6119 | 0.7009 | 67 |
| Idle | 0.5102 | 0.9804 | 0.6711 | 102 |
| Good Picking | 0.9565 | 0.4400 | 0.6027 | 150 |
| Bad Picking | 0.4710 | 0.4740 | 0.4725 | 154 |
| Pushing | 0.9680 | 0.9918 | 0.9798 | 122 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 41 | 16 | 3 | 3 | 4 |
| Idle | 0 | 100 | 0 | 2 | 0 |
| Good Picking | 6 | 1 | 66 | 77 | 0 |
| Bad Picking | 2 | 79 | 0 | 73 | 0 |
| Pushing | 1 | 0 | 0 | 0 | 121 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.6119 | 0.2388 | 0.0448 | 0.0448 | 0.0597 |
| Idle | 0.0000 | 0.9804 | 0.0000 | 0.0196 | 0.0000 |
| Good Picking | 0.0400 | 0.0067 | 0.4400 | 0.5133 | 0.0000 |
| Bad Picking | 0.0130 | 0.5130 | 0.0000 | 0.4740 | 0.0000 |
| Pushing | 0.0082 | 0.0000 | 0.0000 | 0.0000 | 0.9918 |

## Stage 1 — Activity Classification

**Accuracy:** 0.8353

**Macro F1:** 0.8104

**Weighted F1:** 0.8403

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.8298 | 0.5821 | 0.6842 | 67 |
| Idle | 0.5731 | 0.9608 | 0.7179 | 102 |
| Picking | 0.9484 | 0.7862 | 0.8597 | 304 |
| Pushing | 0.9680 | 0.9918 | 0.9798 | 122 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Picking | Pushing |
|---|---:|---:|---:|---:|
| Bending | 39 | 15 | 9 | 4 |
| Idle | 0 | 98 | 4 | 0 |
| Picking | 7 | 58 | 239 | 0 |
| Pushing | 1 | 0 | 0 | 121 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Picking | Pushing |
|---|---:|---:|---:|---:|
| Bending | 0.5821 | 0.2239 | 0.1343 | 0.0597 |
| Idle | 0.0000 | 0.9608 | 0.0392 | 0.0000 |
| Picking | 0.0230 | 0.1908 | 0.7862 | 0.0000 |
| Pushing | 0.0082 | 0.0000 | 0.0000 | 0.9918 |

## Stage 2 — Picking Classification

**Accuracy:** 0.7059

**Macro F1:** 0.6412

**Weighted F1:** 0.6902

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Good Picking | 0.9565 | 0.4400 | 0.6027 | 150 |
| Bad Picking | 0.4620 | 0.4740 | 0.4679 | 154 |
| Other | 0.7636 | 0.9656 | 0.8528 | 291 |

### Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking | Other |
|---|---:|---:|---:|
| Good Picking | 66 | 78 | 6 |
| Bad Picking | 0 | 73 | 81 |
| Other | 3 | 7 | 281 |

### Normalized Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking | Other |
|---|---:|---:|---:|
| Good Picking | 0.4400 | 0.5200 | 0.0400 |
| Bad Picking | 0.0000 | 0.4740 | 0.5260 |
| Other | 0.0103 | 0.0241 | 0.9656 |
