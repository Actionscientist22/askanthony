# Loop through a range of numbers (0 through 4)
for x in range(5):
    print(x)

print("-" * 40)

# Loop through a range of numbers (2 through 6 - yes 6! Up to, but not
# including, 7)
for x in range(2, 7):
    print(x)

print("-" * 40)

# Loop through a range of numbers (0 through 4) without using the value in the
# range
y = 2
for _ in range(5):
    # Add 2 to the value of y
    y += 2
    print(y)

print("-" * 40)

# Iterate through letters in a string
word = "Peace"
for letter in word:
    print(letter)

print("-" * 40)

# Iterate through a list
zoo = ["cow", "dog", "bee", "zebra"]
for animal in zoo:
    print(animal.upper())

print("-" * 40)

# Make changes to each item in a list
numbers = [9, 6, 4, 9]
for i in range(len(numbers)):
    # Add 1 to the list item
    numbers[i] += 1
    print(numbers[i])

print("-" * 40)

# Loop while a condition is being met
run = "y"

# run.lower() means the condition will be met if run = "y" or run = "Y"
while run.lower() == "y":
    print("Hi!")
    run = input("To run again. Enter 'y': ")

# While loop with a Boolean variable
keep_looping = True

while keep_looping:
    print("Hi!")
    keep_looping = bool(input("Press enter to exit and anything else to continue. "))
