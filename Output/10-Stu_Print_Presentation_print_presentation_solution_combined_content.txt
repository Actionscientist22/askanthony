# Declare pi
pi = 3.14159265358979323846

# Print a string that uses the new line character
print("Hello!\nWelcome to Python Class.")

# Ask the user for a name and store it as a variable
full_name = input("Provide the name of someone you would like to speak. ")

# Use an f-string to print the name in title case, along with something they 
# said that uses both single and double quotation marks
print(f"\"They're over there,\" {full_name.title()} said.")

# Ask the user for the number of dashes that should be displayed in the 
# presentation and convert it to an integer
number_of_dashes = int(input("How many dashes would you like to display? "))

# Ask the user for the radius of a circle and convert it to a float
radius = float(input("What radius would you like to use? "))

# Print out the dashes
print("-" * number_of_dashes)

# Use a multiline f-string to print out the radius, surface area, and volume
# of a sphere to 4 decimal places using the radius from the user input.
sphere_details = f"""Radius: {radius}
Surface area: {4 * pi * radius ** 2:.4f}
Volume: {4/3 * pi * radius ** 3:.4f}
"""

print(sphere_details)