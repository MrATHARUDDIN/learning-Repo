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




a = np.array([1, 2, 3, 4], dtype='i4')

print(a)
print(a.dtype)
