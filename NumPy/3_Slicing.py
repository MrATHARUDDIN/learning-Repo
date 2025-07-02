# In NumPy, slicing refers to extracting a portion of an array using a colon syntax similar to Python lists.
# array[start:stop:step]

import numpy as np

a = np.array([12,34,55,52,89,62])
print(a[1:3]) # index 1 to 3rd number
print(a[:4]) # index 0 to 4rd number
print(a[:4:2]) # start with 0 default end at 4rd numbr but count as 2 step at a time (0,2,4,6)
print(a[::2]) # all number as default and count 2 step at a time (0,2,4,6)