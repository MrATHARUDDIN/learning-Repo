import numpy as np

# Generate a 4x4 matrix of random integers between 90 and 99
number = np.random.randint(90, 100, size=(4, 4))
print("Random integers between 90 and 99:")
print(number)

# Generate a 5x10 matrix of binomial distribution samples (n=10, p=0.5)
# Each entry represents the number of successes in 10 trials with a 50% chance
numbers = np.random.binomial(10, p=0.5, size=(5, 10))
print("\nBinomial distribution (n=10, p=0.5):")
print(numbers)

print()

# Generate a 3x3 matrix of random floats from 0.00 to 1.00
matrix = np.random.rand(3, 3)
print("Random floats (0.00 to 1.00):")
print(matrix)

# Scale the values to a range of 0 to 100 and round them to 2 decimal places
scale = np.round(matrix * 100, 2)
print("\nScaled and rounded matrix (0 to 100, 2 decimal places):")
print(scale)


# It will choice number from the array and put in a matrix in 3*3 array 
choice = np.random.choice([10,20,30,40,50] , size=(3,3), replace=True)

# replace=True → allows the same element to be chosen multiple times.
#replace=False → chooses unique elements only (no repetition).

print(choice) 

print("------------------------------------------------")

# Permutation (returns a new shuffled array, original remains unchanged)
arr2 = np.array([1,2,3,4,5,6,7])
shuffled  = np.random.permutation(arr2)
print(f"Orginal Array {arr2}")
print(f"Shuffled Array {shuffled}")