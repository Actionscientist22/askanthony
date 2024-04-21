fish = "halibut"

# Loop through each letter in the string and push to an array
letters = []
for letter in fish:
    letters.append(letter)

print(letters)

# List comprehensions provide concise syntax for creating lists
letters = [letter for letter in fish]

print(letters)

# We can manipulate each element as we go
capital_letters = []
for letter in fish:
    capital_letters.append(letter.upper())

print(capital_letters)

# List comprehension for the above
capital_letters = [letter.upper() for letter in fish]

print(capital_letters)

# We can also add conditional logic (if statements) to a list comprehension
july_temperatures = [87, 85, 92, 79, 106]
hot_days = []
for temperature in july_temperatures:
    if temperature > 90:
        hot_days.append(temperature)
print(hot_days)

# List comprehension with conditional
hot_days = [temperature for temperature in july_temperatures if temperature > 90]

print(hot_days)

# We can also perform calculations in a list comprehension
circle_radii = [2.4, 4.5, 6.2, 7.6, 10.5]
diameters = []
pi = 3.14159265358979323846
for radius in circle_radii:
    diameters.append(2 * pi * radius)
print(diameters)

# List comprehension for the calculation
diameters = [2 * pi * radius for radius in circle_radii]
print(diameters)

# It's even possible to perform list functions on a list comprehension
# Let's find the maximum diameter from our list of radii
max_diameter = max([2 * pi * radius for radius in circle_radii])
print(max_diameter)
