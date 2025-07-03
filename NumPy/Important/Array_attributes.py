import numpy as np

a_mul = np.array([[1,2,3,4],
                [3,4,3,5],
                [5,4,2,1],
                [6,4,5,9],
                [6,4,5,9],
                  ])

print(a_mul.shape) 
# shape will print the row col of the arry
# like here we have 5*4 matrix(array)

print(a_mul.ndim) # 2D
print(a_mul.size) # total number of elements
print(a_mul.dtype) # data type


a = np.array ([[1,3,4],
            ["hello",4,6],
            [7,8,9]
               ])

print(a.dtype) # it will be string cuz in numpy if a single value is string all the array became string
print(type(a[0,1]))
print(a[0,1].dtype)