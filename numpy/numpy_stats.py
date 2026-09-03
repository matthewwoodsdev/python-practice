# NumPy statistics
# Matthew Woods - practice file

import numpy as np

heights = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
weights = np.array([65.4, 59.2, 63.6, 88.4, 68.7])

# mean() - the average
print(np.mean(heights))

# median() - the middle value
print(np.median(heights))

# std() - standard deviation, how spread out the data is
print(np.std(heights))

# corrcoef() - correlation between two arrays
print(np.corrcoef(heights, weights))

# sum() and sort()
print(np.sum(weights))
print(np.sort(weights))

# Generating sample data
np_city = np.random.normal(1.75, 0.20, 5000)
print(np.mean(np_city))
