# NumPy 2D arrays
# Matthew Woods - practice file

import numpy as np

# A list of lists becomes a 2D array
np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
                  [65.4, 59.2, 63.6, 88.4, 68.7]])
print(np_2d)

# shape - rows and columns
print(np_2d.shape)

# Subsetting - [row, column]
print(np_2d[0])
print(np_2d[0][2])
print(np_2d[0, 2])

# Slicing both dimensions at once
print(np_2d[:, 1:3])
print(np_2d[1, :])

# Element-wise maths works here too
bmi = np_2d[1, :] / np_2d[0, :] ** 2
print(bmi)
