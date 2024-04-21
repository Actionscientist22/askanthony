"""Refactoring Examples"""

# Code using for loop.
numbers = [1, 2, 3, 4, 5]
squared_numbers = []
for num in numbers:
    squared_numbers.append(num ** 2)

print(squared_numbers)

# Refactored the code to use a list comprehension
numbers = [1, 2, 3, 4, 5]
squared_numbers = [num ** 2 for num in numbers]

print(squared_numbers)


# Code that uses the range() function.
numbers = [10, 20, 30, 40, 50]
for i in range(len(numbers)):
    print(f"Index: {i}, Value: {numbers[i]}")

# Refactored the code to use enumerate()
numbers = [10, 20, 30, 40, 50]
for i, num in enumerate(numbers):
    print(f"Index: {i}, Value: {num}")


# Code without a function.
numbers = [5, 10, 15, 20, 25]
total = 0
count = 0
for num in numbers:
    total += num
    count += 1
average = total / count
print(f"The average is: {average}")

# Refactored code with a function
def calculate_average(numbers):
    """The function calculates the average of an array of numbers."""
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average

numbers = [5, 10, 15, 20, 25]
average = calculate_average(numbers)
print(f"The average is: {average}")
