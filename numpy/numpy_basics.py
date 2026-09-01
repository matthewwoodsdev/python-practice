# NumPy basics
# Matthew Woods - practice file

import numpy as np

# Creating an array from a list
heights = [1.73, 1.68, 1.71, 1.89, 1.79]
np_heights = np.array(heights)
print(np_heights)

# Arrays do element-wise maths, lists don't
weights = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
bmi = weights / np_heights ** 2
print(bmi)

# Comparison returns an array of True/False
print(bmi > 23)

# Subsetting with that boolean array
print(bmi[bmi > 23])

# Single element by index
print(bmi[1])
