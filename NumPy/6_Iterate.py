import numpy as np

# 1D array
a = np.array([1,2,3,4,5])
for x in a:
    print(x)

# 2D array
arr = np.array([[1,2,3],[4,5,6]])

for x in arr:
    for y in x:
        print(y)

# 3D array 
c = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])  # Shape: (2, 2, 2)

print("----------------")
for x in c:
    for y in x:
        for z in y:
            print(z)

# Iterating With Different Step Size

print("-----------Iterating With Different Step Size------------------")

d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in d[::2]: # skip by 1
    print(x)