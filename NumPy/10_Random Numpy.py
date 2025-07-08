import numpy as np

number = np.random.randint(90, 100, size=(4,4))
print(number)

numbers = np.random.binomial(10, p=0.5, size=(5,10))
print(numbers)



print()
matrix = np.random.rand(3,3) # np.random.rand(shape) # it's will put random number form 0.00 to 1.00
scale = np.round(matrix*100,2) # it will round the value 
# Means it will take 2 decimal number
print(scale)

