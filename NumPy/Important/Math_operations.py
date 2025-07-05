import numpy as np
l1 = [1,2,3,4,5]
l2 = [6,7,8,9,5]

a1 = np.array(l1)
a2 = np.array(l2)

print(l1 * 5) # with python list
print(a1 * 5) # with Numpy list

# in python it just print the list 5 time
# in numpy it will work as a matrix

print(a1 + 5)
print(a1 + a2)
print(a1 * a2)

print("------------------------")
a1 = np.array([1,2,3])
a2 = np.array([[1],[2]])

print(a1 + a2)

print("-----------Root elements -------------")

a = np.array([[16,2,3],[4,5,100]])
print(np.sqrt(a))
# similarly we can use sin,cos,tan,arcsin etc method with our matrix