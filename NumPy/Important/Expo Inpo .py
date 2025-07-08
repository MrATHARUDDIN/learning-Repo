import numpy as np

# --- Part 1: Using .npy ---
a = np.array([
    [1,2,3,4,5,6],
    [7,8,9,10,11,12],
    [13,14,15,16,17,18],
    [18,19,20,21,22,23],
])

np.save("myarray.npy", a)         # Saves array 'a' to a binary file
n = np.load("myarray.npy")        # Loads it back into memory
print(n)                          # Prints the array


# --- Part 2: Using .csv ---
b = np.array([[1,2,3],[4,5,6]])

np.savetxt("array.csv", b, delimiter=",", fmt="%d")  # Saves array 'b' as CSV
loaded = np.loadtxt("array.csv", delimiter=",")      # Loads it back
print(loaded)                                         # Prints the loaded array



# Important Tips:

# 🔸 .npy:
# Very fast and efficient.
# Keeps shape and data type.
# Not human-readable.
# Use when working only in Python or with large data.

#🔸 .csv:
# Human-readable, can be opened in Excel or Notepad.
# Good for sharing data outside Python.
# Loses dtype and some shape info (e.g., can’t save 3D arrays easily).
# Use fmt="%d" for integers, %f for floats, etc.