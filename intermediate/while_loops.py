# While loops
# Matthew Woods - practice file

# A while loop repeats as long as its condition stays True
x = 1

while x < 4:
    print(x)
    x = x + 1

# The condition is checked before every pass
# Once x reaches 4, the loop stops and the program moves on
print("Done counting")

# Counting down instead
countdown = 3

while countdown > 0:
    print(countdown)
    countdown = countdown - 1

print("Liftoff!")

# Shrinking an error value - a classic DataCamp example
error = 50.0

while error > 1:
    error = error / 4
    print(error)

# Careful: if the condition never becomes False, the loop runs forever
# The line that changes the variable is what stops it
# Leave out "x = x + 1" above and the loop never ends
