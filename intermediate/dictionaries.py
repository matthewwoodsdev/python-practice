# Dictionaries
# Matthew Woods - practice file

# A dictionary stores pairs - a key, and the value it points to
capitals = {"ireland": "dublin", "france": "paris", "spain": "madrid"}

print(capitals)

# You look things up by key, not by position
print(capitals["ireland"])

# Adding a new pair
capitals["italy"] = "rome"
print(capitals)

# Changing an existing value - same syntax as adding
capitals["spain"] = "barcelona"
print(capitals)

# Removing a pair
del capitals["spain"]
print(capitals)

# Checking whether a key is there
print("france" in capitals)
print("germany" in capitals)

# Getting all the keys, or all the values
print(capitals.keys())
print(capitals.values())

# Looping over a dictionary needs .items()
for country, capital in capitals.items():
    print("the capital of " + country + " is " + capital)

# Values can be any type, including another dictionary
europe = {
    "ireland": {"capital": "dublin", "population": 5.1},
    "france": {"capital": "paris", "population": 68.0}
}

print(europe["ireland"]["capital"])
print(europe["france"]["population"])
