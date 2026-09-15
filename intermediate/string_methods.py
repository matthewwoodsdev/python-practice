# String methods
# Matthew Woods - practice file

name = "Matthew Woods"

# Changing case
print(name.upper())
print(name.lower())

# Length
print(len(name))

# Finding and counting
print(name.count("o"))
print(name.index("W"))

# Replacing part of a string
print(name.replace("Woods", "W."))

# Splitting a string into a list
print(name.split(" "))

# Stripping whitespace off the ends
messy = "   hello   "
print(messy.strip())

# Checking how a string starts or ends
print(name.startswith("Matt"))
print(name.endswith(".py"))

# f-strings - the modern way to build a string
course = "Software Development Level 5"
print(f"{name} is starting {course}")
