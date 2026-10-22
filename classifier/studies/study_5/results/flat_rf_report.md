# Flat Architecture - Random Forest

## Final Performance

**Accuracy:** 0.6837

**Macro F1:** 0.6997

**Weighted F1:** 0.6806

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.8700 | 0.6493 | 0.7436 | 134 |
| Idle | 0.5184 | 0.9657 | 0.6747 | 204 |
| Good Picking | 0.9128 | 0.4518 | 0.6044 | 301 |
| Bad Picking | 0.4858 | 0.4984 | 0.4920 | 309 |
| Pushing | 0.9797 | 0.9877 | 0.9837 | 244 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 87 | 32 | 8 | 4 | 3 |
| Idle | 3 | 197 | 0 | 3 | 1 |
| Good Picking | 6 | 2 | 136 | 156 | 1 |
| Bad Picking | 2 | 148 | 5 | 154 | 0 |
| Pushing | 2 | 1 | 0 | 0 | 241 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.6493 | 0.2388 | 0.0597 | 0.0299 | 0.0224 |
| Idle | 0.0147 | 0.9657 | 0.0000 | 0.0147 | 0.0049 |
| Good Picking | 0.0199 | 0.0066 | 0.4518 | 0.5183 | 0.0033 |
| Bad Picking | 0.0065 | 0.4790 | 0.0162 | 0.4984 | 0.0000 |
| Pushing | 0.0082 | 0.0041 | 0.0000 | 0.0000 | 0.9877 |
