import numpy as np

print(np.nan)
print(np.inf)
# np.nan: This is "Not a Number"
# np.inf: This is infinity


print(np.isnan(np.nan))
print(np.isinf(np.inf))
# np.isnan(np.nan): Checks if the value is NaN → returns True.
# np.isinf(np.inf): Checks if the value is infinite → returns True.



print(np.isnan(np.sqrt(-1))) # square root of a nagative number is not a real number
print(np.isinf(np.array([10])/0)) # 10 devided by 0 give us infinity 