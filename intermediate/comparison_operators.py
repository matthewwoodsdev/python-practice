# Comparison and boolean operators
# Matthew Woods - practice file

# Numeric comparisons return True or False
print(5 > 3)
print(5 >= 5)
print(10 < 2)
print(3 == 3)
print(3 != 3)

# Comparisons work on strings too, alphabetically
print("apple" < "banana")

# You can compare variables
age = 21
print(age >= 18)

# and - both sides must be True
print(True and True)
print(True and False)

# or - at least one side must be True
print(True or False)
print(False or False)

# not - flips the value
print(not True)

# Combining them in a condition
temperature = 15
is_raining = False

print(temperature > 10 and not is_raining)

# With numpy arrays, use logical_and instead of and
import numpy as np

heights = np.array([1.73, 1.68, 1.89, 1.55])
print(np.logical_and(heights > 1.60, heights < 1.80))
