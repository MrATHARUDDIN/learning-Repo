# NumPy is a Python library.
# NumPy is used for working with arrays.
# NumPy is short for "Numerical Python".

# First, we import the NumPy library with the alias 'np'
import numpy as np

# Normal 1D Array
# This creates a one-dimensional NumPy array containing the elements 1 through 5
arr = np.array([1, 2, 3, 4, 5])
print(arr)  # Output: [1 2 3 4 5]
print()     # Prints an empty line for better readability

# 2D Array
# This creates a two-dimensional array (a matrix) with 2 rows and 3 columns
delo = np.array([[1, 2, 3], [4, 5, 6]])
print(delo)
# Output:
# [[1 2 3]
#  [4 5 6]]

# 3D Array
# This creates a three-dimensional array (2 blocks, each with 2 rows and 3 columns)
third_arr = arr = np.array([
    [[1, 2, 3], [4, 5, 6]],  # First block (2D array)
    [[1, 2, 3], [4, 5, 6]]   # Second block (2D array)
])
# Checking and printing the number of dimensions of the array
print(third_arr.ndim)  # Output: 3 (it's a 3-dimensional array)

# Another 3D Array
# Slightly different values, but still 3D structure: 2 blocks, each with 2 rows and 3 columns
d = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[1, 4, 3], [4, 5, 6]]
])
print(d.ndim)  # Output: 3
