# NumPy is a Python library.
# NumPy is used for working with arrays.
# NumPy is short for "Numerical Python".


import numpy as np

# Normal 1D Array

arr = np.array([1, 2, 3, 4, 5])
print(arr)  # Output: [1 2 3 4 5]
print()    

# 2D Array

delo = np.array([[1, 2, 3], [4, 5, 6]])
print(delo)


# 3D Array

third_arr = arr = np.array([
    [[1, 2, 3], [4, 5, 6]],  # First block (2D array)
    [[1, 2, 3], [4, 5, 6]]   # Second block (2D array)
])
print(third_arr.ndim)  # Output: 3 (it's a 3-dimensional array)

# Another 3D Array
d = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[1, 4, 3], [4, 5, 6]]
])
print(d.ndim)  # Output: 3
