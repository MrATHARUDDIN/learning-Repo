# Pandas DataFrame Memory Usage Guide

## Overview
When working with large datasets, it’s important to monitor memory usage. Pandas provides a convenient method to check the memory usage of each column in a DataFrame.

---

## Method: `DataFrame.memory_usage()`

### Syntax:
```python
DataFrame.memory_usage(index=True, deep=False)
