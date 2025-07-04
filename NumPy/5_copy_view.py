# The main difference between a copy and a view of a NumPy array:
# ✅ Copy → Creates a new array in memory. Changes in the copy do NOT affect the original.
# 🔁 View → Only creates a reference to the original array. Changes in the view DO affect the original.

import numpy as np

# ----------- Example with COPY -----------
a = np.array([1, 2, 4])

b = a.copy() 
b[2] = 3     

print(f"Original array : {a}")  # Output: [1 2 4]
print(f"Copy array     : {b}")  # Output: [1 2 3]


# ----------- Example with View -----------
c = np.array([2, 4, 6])
d = c.view()  
d[2] = 8      

print(f"Original array : {c}")  # Output: [2 4 8]
print(f"Copy array     : {d}")  # Output: [2 4 8]

# 💡 Summary:
# - copy() → Independent array; safe from unwanted changes.
# - view()  → Shares data with original; changes will affect both new and orginal array.
