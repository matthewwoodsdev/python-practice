# For loops
# Matthew Woods - practice file

# A for loop walks through a list, one item at a time
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

for area in areas:
    print(area)

# The variable name between for and in is yours to choose
for a in areas:
    print(a)

# enumerate gives you the position as well as the item
for index, area in enumerate(areas):
    print("room " + str(index) + ": " + str(area))

# Looping over a string gives one character at a time
for letter in "Matthew":
    print(letter)

# Looping over a nested list
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["bedroom", 10.75]]

for room in house:
    print("the " + room[0] + " is " + str(room[1]) + " sqm")

# Unpacking the two parts directly
for name, area in house:
    print("the " + name + " is " + str(area) + " sqm")
