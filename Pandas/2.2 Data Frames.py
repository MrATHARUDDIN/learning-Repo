import pandas as pd

df = pd.DataFrame({
    "name":["Mike","Bob","Alice"],
    "age":[17,20,30],
    "job":["IT","Forex","Real"]
})

# Set 'name' as the index
df = df.set_index("name")
print("🔹 Original DataFrame:")
print(df)
print()
print("##################################  Filtering Data Frames by age > 18  #############################################")

################################################################################################
# filter the data by using contions
over_18 = df[df["age"] > 18]      # varname[varname["info that filter by"]condition]
print(over_18)

print("################################  Adding and removing column  ################################################################")
# Adding and Removing Columns
df["City"] = ["pistoia","Florence","Pisa"]
print(df)

df.drop("City",axis=1,inplace=True)
print(df)

# DataFrame.ndim 
# it will show us the dimantion of the dataframe (array)
print(df.ndim)

print("################################  Modifying Data  ################################################################")
dff = pd.DataFrame({
    "name":["Mike","Bob","Alice"],
    "age":[17,34,30],
    "job":["IT","Forex","Real"]
})
dff.at[0,"name"] = "Athar" # Modify a single vlaue

dff["age"] = dff["age"]+1 # updating everyone age by 1
print(dff)


print("################################  Sorting Data  ################################################################")
dff = dff.sort_values("age", ascending=False) # biger to small
dff = dff.sort_values("age") # small to big

print(dff)


print("################################  Group Data  ################################################################")
student = pd.DataFrame({
    "name":["Mike","Ena","Alice","Ali","Mama","Kala"],
    "age":[17,34,30,20,34,32],
    "job":["IT","Forex","Forex","IT","Medical","Medical"]
})

grouped = student.groupby("job")["age"].mean() # Group by 'job' and calculate average age per job
print(grouped)

for jobs,group in student.groupby("job"):
    print(f"work in {jobs}")
    print(group)