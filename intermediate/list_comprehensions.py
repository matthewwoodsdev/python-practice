# List comprehensions
# Matthew Woods - practice file

# The long way - a loop that builds a list
numbers = [1, 2, 3, 4, 5]
doubled = []

for n in numbers:
    doubled.append(n * 2)

print(doubled)

# The same thing as a comprehension
doubled = [n * 2 for n in numbers]
print(doubled)

# Read it as: do this, for each item, in this list
squares = [n ** 2 for n in numbers]
print(squares)

# It works on strings too
names = ["matthew", "sarah", "john"]
capitalised = [name.upper() for name in names]
print(capitalised)

# Adding a condition on the end filters what goes in
evens = [n for n in numbers if n % 2 == 0]
print(evens)

# Condition and calculation together
big_evens = [n * 10 for n in numbers if n % 2 == 0]
print(big_evens)

# Building from a range
first_ten = [n for n in range(10)]
print(first_ten)

# Same idea with a dictionary
lengths = {name: len(name) for name in names}
print(lengths)
