# Declare variables
x = 1
y = 10

# Check if one value is equal to another
if x == 1:
    print("x is equal to 1")

# Check if one value is NOT equal to another
if y != 1:
    print("y is not equal to 1")

# Check if one value is less than another
if x < y:
    print("x is less than y")

# Check if one value is greater than another
if y > x:
    print("y is greater than x")

# Check if a value is greater than or equal to another
if x >= 1:
    print("x is greater than or equal to 1")

# Use a Boolean to check a condition
congratulations = True
#congratulations = False

if congratulations:
    print("Congratulations!")
else:
    print("How are you feeling?")

# Get an input from a user
user_input = input("What number would you like to check? ")

# Check if the user input is a number
if user_input.isdigit():
    number = int(user_input)
    print(f"Input '{number}' is a number!")
else:
    print(f"{user_input} is not a number.")