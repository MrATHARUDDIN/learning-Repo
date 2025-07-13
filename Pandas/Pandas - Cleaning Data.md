## Pandas - Cleaning Data
- Data cleaning means fixing bad data in your data set.

## Types of Bad Data:
- **Empty Cells:** Missing values in cells.
- **Data in Wrong Format:** Values that don’t match the expected data type or structure.
- **Wrong Data:** Values that are incorrect or out of range.
- **Duplicates:** Repeated rows that can skew analysis results.

---

## Handling Empty Cells

### Why Empty Cells Matter:
Empty cells can potentially give you incorrect results during data analysis. It’s important to handle them properly.

---
#### 1. Remove Rows with Empty Cells
If the dataset is large, removing a few rows may not impact overall analysis.

```python
import pandas as pd

df = pd.read_csv('data.csv')

# Remove rows with any empty cells
df.dropna(inplace=True)


- Another way of dealing with empty cells is to insert a new value instead.

# Fill all empty cells with 0
df.fillna(0, inplace=True)

# Fill all empty cells with a string
df.fillna('Unknown', inplace=True)
