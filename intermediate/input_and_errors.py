# Input and handling errors
# Matthew Woods - practice file

# input() pauses and waits for the person to type something
name = input("What is your name? ")
print("Hello, " + name)

# Whatever comes back from input() is always a string
age = input("How old are you? ")
print(type(age))

# So you convert it if you need a number
age = int(age)
print(age + 1)

# But if they type "twenty", int() crashes the program
# try/except catches that instead

number = input("Give me a number: ")

try:
    number = int(number)
    print("Doubled, that is " + str(number * 2))
except ValueError:
    print("That was not a number.")

# The same pattern guards against dividing by zero
try:
    print(10 / 0)
except ZeroDivisionError:
    print("You cannot divide by zero.")

# else runs when nothing went wrong, finally runs either way
try:
    total = 10 / 2
except ZeroDivisionError:
    print("Something went wrong.")
else:
    print("That worked: " + str(total))
finally:
    print("Done either way.")
