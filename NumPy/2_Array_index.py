import numpy as np

a = np.array([1,2,3]) # 1D array
print(a[0]) # index start with 0 and it the position of an array value

b = np.array([[1,3,5],
              [2,5,6]])
print(b[1,0]) # row number 1(index) colum number 0(index)  # 2

c = np.array([[1,3,4],[3,8,9],[18,23,45]])
print(c[2,1])

d = np.array([[1,3,4],[3,8,9],[18,43,46],[34,65,64]])
print(d[3,2])