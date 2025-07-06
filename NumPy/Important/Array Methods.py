import numpy as np

a = np.array([1,2,3])  # main array

a = np.append(a, [7,8,9])  # append values

a = np.insert(a, 3, [4,5,6])  # insert [4,5,6] at index 3

a = np.delete(a, 0)  # delete value at index 0

print(a)

