# If, elif and else
# Matthew Woods - practice file

# if runs its block only when the condition is True
z = 4

if z % 2 == 0:
    print("z is even")

# else catches everything the if did not
z = 5

if z % 2 == 0:
    print("z is even")
else:
    print("z is odd")

# elif adds more conditions, checked in order
z = 6

if z % 2 == 0:
    print("z is divisible by 2")
elif z % 3 == 0:
    print("z is divisible by 3")
else:
    print("z is neither divisible by 2 nor 3")

# Only the first True branch runs - 6 fits both, but 3 never gets checked

# Using a comparison you have already met
room = "kit"

if room == "kit":
    print("Looking around the kitchen.")
else:
    print("Looking around elsewhere.")

# Numbers work the same way
area = 14.0

if area > 15:
    print("Big place!")
elif area > 10:
    print("Medium size, nice!")
else:
    print("Pretty small.")
