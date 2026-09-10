# Filtering pandas DataFrames
# Matthew Woods - practice file

import pandas as pd

# A small DataFrame to filter
data = {
    "country": ["Ireland", "France", "Spain", "Italy"],
    "capital": ["Dublin", "Paris", "Madrid", "Rome"],
    "area": [70.3, 551.7, 505.9, 301.3],
    "population": [5.1, 68.0, 47.4, 59.0]
}

countries = pd.DataFrame(data)
countries.index = ["IE", "FR", "ES", "IT"]

print(countries)

# Step 1 - get the column you want to test
areas = countries["area"]
print(areas)

# Step 2 - compare it, which gives True or False per row
big = areas > 400
print(big)

# Step 3 - use that as the filter
print(countries[big])

# The same thing in one line
print(countries[countries["area"] > 400])

# Filtering on a different column
print(countries[countries["population"] < 50])

# Two conditions at once - use logical_and from numpy
import numpy as np

print(countries[np.logical_and(countries["area"] > 300, countries["area"] < 520)])
