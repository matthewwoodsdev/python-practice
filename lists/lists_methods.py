# List methods
# Matthew Woods - practice file

areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# index() - find where a value sits
print(areas.index(20.0))

# count() - how many times a value appears
print(areas.count(9.50))

# append() - add to the end
areas.append(24.5)
print(areas)

# remove() - delete the first matching value
areas.remove(18.0)
print(areas)

# reverse() - flips the list in place
areas.reverse()
print(areas) 
