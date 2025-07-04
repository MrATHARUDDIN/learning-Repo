import numpy as np

a= np.full((2,3),9) # np.full((rows, columns), value)
print(a)
# Output:
# [[9 9 9]
#  [9 9 9]]

b = np.zeros((2,3,3)) # np.zeros((depth, rows, columns))
print(b)  # Output: array of all zeros with shape (2, 3, 3)
 



# np.empty creates an array without filling it with zeros or ones
c = np.empty((2,2,2))
print(c) # np.empty creates an array without filling it with zeros or ones

