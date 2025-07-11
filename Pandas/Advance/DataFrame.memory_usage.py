import pandas as pd

data = {
    'A': [1, 2, 3],
    'B': ['x', 'y', 'z']
}

df = pd.DataFrame(data)

# Basic memory usage
print(df.memory_usage())

# Memory usage including deeper inspection for object types
print(df.memory_usage(index=True, deep=False))
