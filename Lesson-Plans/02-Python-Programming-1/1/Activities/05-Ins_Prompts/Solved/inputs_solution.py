# Collect the user's input for the prompt "What is your name?"
user_name = input("What is your name? ")

# Print the data type of user_name
print("user_name is type", type(user_name))

# Collect the user's input for the prompt "How old are you?" and convert the
# string to an integer.
age = int(input("How old are you? "))

# Print the data type of age
print("age is type", type(age))

# Collect the user's input for the prompt "What is your average weekly grocery 
# bill?" and convert the string to a float.
grocery_bill = float(input("What's your average weekly grocery bill? "))

# Print the data type of grocery_bill
print("grocery_bill is type", type(grocery_bill))

# Collect the user's input for the prompt "Will you type an input?" and
# convert it to a boolean. Note that non-zero, non-empty objects return True.
true_or_false = bool(input("Will you type an input? "))

# Print the data type of true_or_false
print("true_or_false is type", type(true_or_false))

# Create four print statements that displays text about the user's inputs
print("My name is " + user_name)
print("I am " + str(age) + " years old.")
print("I spend an average of $" + str(grocery_bill) + " per week on groceries")
print("The input was converted to " + str(true_or_false))
