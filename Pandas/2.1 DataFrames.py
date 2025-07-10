import pandas as pd

# New dataset with more realistic data
data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva","Athar","colombo","Taskin","Juhan"],
    "age": [24, 27, 22, 32, 29,17,17,16,18],
    "city": ["Rome", "Milan", "Naples", "Florence", "Turin","Pistoia","Pistoia","Stockwhlome","New Yok"]
}

df = pd.DataFrame(data)

print("🔹 Full DataFrame:")
print(df)

print("\n🔹 First 5 rows:")
print(df.head())

print("\n🔹 Last 5 rows:")
print(df.tail())

print("\n🔹 Shape (rows, columns):")
print(df.shape)

print("\n🔹 Info :") #Info about data types and non-null counts
print(df.info())

print("\n🔹Print all Columns name :")
print(df.columns)

print("\n🔹 Row indexes:") # show row index list
print(df.index)

################################################################################################

df["name"]           # Access a single column (as Series)
df[["name", "age"]]  # Access multiple columns

df.loc[0]            # Access row by label/index
df.iloc[0]           # Access row by position
df.loc[0, "name"]    # Access specific cell

