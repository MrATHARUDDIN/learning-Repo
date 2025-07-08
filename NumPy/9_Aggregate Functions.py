import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9])

print("Sum:", np.sum(arr))                 # Total sum
print("Mean:", np.mean(arr))               # Average
print("Median:", np.median(arr))           # Middle value
print("Min:", np.min(arr))                 # Smallest value
print("Max:", np.max(arr))                 # Largest value
print("Standard Deviation:", np.std(arr))  # Spread of values
print("Variance:", np.var(arr))            # Squared spread
print("Product:", np.prod(arr))            # Product of all elements
print("Size:", np.size(arr))               # Number of elements
print("Count of non-zero:", np.count_nonzero(arr))  # Non-zero count


mat = np.array([[1, 2, 3], [4, 5, 6]])

print("Row-wise sum:", np.sum(mat, axis=1))
print("Column-wise sum:", np.sum(mat, axis=0))
print("Row-wise mean:", np.mean(mat, axis=1)) # avg
print("Column-wise max:", np.max(mat, axis=0))
