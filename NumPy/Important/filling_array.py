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


# Generate a 1D array of even numbers from 0 to 98 (step of 2)
x_values = np.arange(0, 100, 2)  # np.arange(start, stop, step)
print(x_values)
# Output: [ 0  2  4  6 ... 96 98]


# Generate 6 evenly spaced values between 0 and 100 (inclusive)
x_values = np.linspace(0, 100, 6)  # np.linspace(start, stop, number_of_points)
print(x_values)
# Output: [  0.  20.  40.  60.  80. 100.]