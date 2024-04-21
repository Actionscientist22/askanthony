fish = "halibut"

# Loop through each letter in the string and push to an array
letters = []
for letter in fish:
    letters.append(letter)

print(letters)

# List comprehensions provide concise syntax for creating lists


# We can manipulate each element as we go
capital_letters = []
for letter in fish:
    capital_letters.append(letter.upper())

print(capital_letters)

# List comprehension for the above


# We can also add conditional logic (if statements) to a list comprehension
july_temperatures = [87, 85, 92, 79, 106]
hot_days = []
for temperature in july_temperatures:
    if temperature > 90:
        hot_days.append(temperature)
print(hot_days)

# List comprehension with conditional


# We can also perform calculations in a list comprehension
circle_radii = [2.4, 4.5, 6.2, 7.6, 10.5]
diameters = []
pi = 3.14159265358979323846
for radius in circle_radii:
    diameters.append(2 * pi * radius)
print(diameters)

# List comprehension for the calculation


# It's even possible to perform list functions on a list comprehension
# Let's find the maximum diameter from our list of radii

