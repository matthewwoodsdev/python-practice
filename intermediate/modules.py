# Modules
# Matthew Woods - practice file

# A module is a Python file containing functions and attributes
import os

# type() shows it is a module
print(type(os))

# getcwd() - get the current working directory
print(os.getcwd())

# Store it so it can be referenced later
work_dir = os.getcwd()

# chdir() - change directory
os.chdir("/home")
print(os.getcwd())

# work_dir still holds the original path
print(work_dir)

# Attributes return values - no parentheses
print(os.environ)

# The string module simplifies text processing
import string

print(string.ascii_lowercase)
print(string.digits)
print(string.punctuation)
