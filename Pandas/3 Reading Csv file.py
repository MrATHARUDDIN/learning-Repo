import pandas as pd

# Read Csv file
df = pd.read_csv("csv/footballer.csv")

dff = pd.DataFrame(df)

# adding new player
new_index = len(dff)
dff.loc[new_index] = ["Kylian Mbappé", 53, 1, 25, 80]
# use DataFrame.loc[index] = [value]


filters = dff[dff["Total Goals"] > 50]
#df[df['column'] > value] — Filter rows based on condition.



print(filters)