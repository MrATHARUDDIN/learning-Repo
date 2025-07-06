import numpy as np

a = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
              ])
print(a.shape) # 4*5
print(a.reshape((5,4))) # reshaping 4*5 -->  5*4
print(a.reshape((2,2,5))) #reshaping 4*5 --> 2 List 2*5

print("----------------------------")
print(a.flatten()) # flat arry in 1D
print(a.ravel())
print("---------- With flatten ------------------")
var1 = a.flatten()
var1[2] = 100 # only var1 changed
print(var1)
print(a)

print("---------- With ravle ------------------")
var2 = a.ravel()
var2[2] = 100 # var2 changed, and `a` is now updated too!
print(var2) 
print(a)

# flatten() # Returns a **copy** of the array in 1D
# ravel()   # Returns a **view** of the array in 1D (if possible)
print()
print("--------------Swipe value -----------------")
print()
b = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
              ])
print(b.swapaxes(0,1)) # row is now collomn and col is row


b = np.array([[1,2,3],[5,6,7]])
print(b.T) # same work as Swapaxes

