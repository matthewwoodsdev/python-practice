# Slicing lists
# Matthew Woods - practice file

fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]

# [start:end] - start is included, end is not
print(fam[3:5])
print(fam[1:4])

# Leaving one side blank
print(fam[:4])
print(fam[5:])
print(fam[:])

# Negative index slicing
print(fam[-4:])
print(fam[:-2])

# Step - every second item
print(fam[::2])

# Reverse a list with a step of -1
print(fam[::-1]) 
