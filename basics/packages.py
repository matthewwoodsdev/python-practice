# Packages
# Matthew Woods - practice file

# import - brings in the whole package
import math

r = 0.43
C = 2 * math.pi * r
A = math.pi * r ** 2

print("Circumference:", C)
print("Area:", A)

# from ... import - brings in one piece only
from math import pi

print(pi)

# import ... as - gives the package a shorter name
import numpy as np

heights = np.array([1.73, 1.68, 1.71, 1.89])
print(heights) 
print(heights.mean()) 
print(heights.mean())
