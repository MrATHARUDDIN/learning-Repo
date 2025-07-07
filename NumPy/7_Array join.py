import numpy as np

# joing 1D array
a = np.array([1,2,3,4])
b = np.array([5,9,7,6])

arr = np.concatenate((a,b))
print(arr)

# joing 2D array 
print("-------------------------------------------")
arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[7,8,9],[10,11,12]])

arr3 = np.concatenate((arr1,arr2)) # add the new array as row (or we can say  in axis = 0)
arr4 = np.concatenate((arr1,arr2), axis=1) 
# axis means the row will be same as before but we just
# insert new valus as collumn 

print(arr3) # axis 0
print(arr4) # axis 1

# Array Join with stack # using stack on 1D arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)         # create pairs column-wise
print(arr)