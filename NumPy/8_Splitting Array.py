import numpy as np

# ------------------------ 1D Array ------------------------
arr = np.array([1, 2, 3, 4, 5, 6])  # 1D array

newarr = np.array_split(arr, 3)  # split array into 3 sub-arrays
# This splits the original array into 3 sub-arrays as evenly as possible

print(newarr)

print(newarr[0])  
print(newarr[1])
print(newarr[2])

# ------------------------ 2D Array ------------------------
print("-------------- 2D Array -------------------")

a = np.array([[1, 2], 
              [3, 4],
              [5, 6],
              [7, 8], 
              [9, 10],
              [11, 12]])  # 2D array with 6 rows and 2 columns

newa = np.array_split(a, 3)  # split 2D array into 3 sub-arrays (along rows)
# This splits the 2D array into 3 sub-arrays, each containing 2 rows

print(newa)  # list of 3 sub-arrays
print(newa[0])
print(newa[1])
print(newa[2])

# Split 2D array along columns (axis=1)
newb = np.array_split(a, 3, axis=1)  
# This splits the array into 3 sub-arrays on the columns (each will have fewer columns)

print(newb)

# Print the shape of each sub-array in newb
print("Shapes of arrays in newb:")
for i, arr in enumerate(newb):
    print(f"Shape of newb[{i}]:", np.shape(arr))

# hsplit means with axis 1 (create pairs in column)
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.hsplit(arr, 3)
print(newarr)