# Custom functions
# Matthew Woods - practice file

# def creates a function - the body is indented
def greet():
    print("Hello!")

# Nothing happens until you call it
greet()

# Arguments let you pass values in
def greet_user(name):
    print("Hello, " + name + "!")

greet_user("Matthew")

# return sends a value back out
def add(a, b):
    return a + b

total = add(4, 6)
print(total)

# Default arguments are used when none is given
def greet_default(name="there"):
    print("Hello, " + name + "!")

greet_default()
greet_default("Matthew")

# A docstring explains what the function does
def average(numbers):
    """Return the average of a list of numbers."""
    return sum(numbers) / len(numbers)

print(average([11.25, 18.0, 20.0]))
print(average.__doc__)
