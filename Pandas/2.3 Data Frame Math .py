import pandas as pd

# First dataset
Data = {
    "name": ["Athar", "Sabbir", "Dip", "Shihab"],
    "age": [17, 18, 19, 19],
    "job": ["IT", "Medical", "Business", "Business"]
}

df = pd.DataFrame(Data)

# Second dataset
newData = {
    "name": ["Azhar", "bk"],
    "age": [34, 45],
    "job": ["IT", "Medical"]
}

new_df = pd.DataFrame(newData)

# Concatenate both DataFrames
kk = pd.concat([df, new_df], ignore_index=True)
print(kk)
