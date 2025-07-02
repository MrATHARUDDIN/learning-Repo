


# Below is a list of all data types in NumPy and the characters used to represent them.

# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
student = np.array(["Athar", "Sabbir", "Nasir", "Leo"])

print(arr.dtype)      # Output: int64 (or int32, depending on your system)
print(student.dtype)  # Output: <U6 (Unicode string of max length 6)



a = np.array([1, 2, 3, 4], dtype='i4') # i4 means integer 4 bytes = 32bit
#                                        This means each number in the array is stored using 4 bytes of memory

print(a)         # Output: [1 2 3 4]
print(a.dtype)   # Output: int32


# Why Use Custom Data Types?

# Save memory (e.g., use i1 if values are small)
# Match external data (like from files or databases)
# Optimize speed for large-scale numerical operations


################## Converting data Type (type Casting in numpy)  ################## 
# Converting data type means changing the type of elements in an existing array to another type—like converting an array of integers to floats, or strings to integers (if possible).

#In NumPy, you do this using the .astype() method.


c = np.array([1,2,3,4,5])
print(c.dtype)

floatarr = c.astype("float32") # so with astype we can swipe the value
print(floatarr.dtype)