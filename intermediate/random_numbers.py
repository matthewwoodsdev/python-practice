# Random numbers
# Matthew Woods - practice file

import numpy as np

# A seed makes random results repeatable
np.random.seed(123)

# random() gives a float between 0 and 1
print(np.random.rand())
print(np.random.rand())

# randint(a, b) gives a whole number from a up to but not including b
print(np.random.randint(1, 7))

# Simulating a dice roll
dice = np.random.randint(1, 7)
print("You threw a " + str(dice))

# Using the roll to decide what happens next
step = 50

if dice <= 2:
    step = step - 1
elif dice <= 5:
    step = step + 1
else:
    step = step + np.random.randint(1, 7)

print("After the throw, step is " + str(step))

# Rolling many times with a loop
rolls = []

for i in range(10):
    rolls.append(np.random.randint(1, 7))

print(rolls)
