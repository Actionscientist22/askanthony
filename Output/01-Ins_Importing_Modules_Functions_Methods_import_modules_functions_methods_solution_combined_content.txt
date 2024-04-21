"""Importing  modules, functions and methods"""

# Import the sqrt function from the math module.
from math import sqrt

# Calculate the square root of a number.
number = 16
result = sqrt(number)
print(f"The square root of {number} is {result}")


# Import the randint and choice methods from the random module.
from random import randint, choice

# Generate a random number between 1 and 10 and selecting a random element from a list.
random_number = randint(1, 10)
print(f"The random number is: {random_number}")

my_list = ['apple', 'banana', 'orange', 'grape', 'mango']

# Use the choice method to randomly select an element from the list.
random_element = choice(my_list)
print(f"A random element from the list is: {random_element}")

# Import the datetime and date classes from the datetime module.
from datetime import datetime, date

# Get the current datetime using the now function.
current_datetime = datetime.now()
# Get the current time using the strftime function.
current_time = current_datetime.strftime("%H:%M:%S")
# Get the current date using the today function.
current_date = date.today()

print(f"The current datetime is: {current_datetime}")
print(f"The current time is: {current_time}")
print(f"The current date is: {current_date}")
