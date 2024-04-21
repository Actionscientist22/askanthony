# Anonymous Functions

# A function that divides by 7 and rounds to the nearest hundredth
def divide_by_seven(num):
    """A function that divides by 7 and rounds to the nearest hundredth"""
    return round(num / 7,3)
print(f"The result of using a Python function: {[divide_by_seven(number) for number in [24,654,3,961,21]]}")


# Create a list comprehension that divides by 7 and rounds to the nearest hundredth
list_comprehension = [divide_by_seven(number) for number in [24,654,3,961,21]]

# Print the results
print(f"An example of a list comprehension that uses a function: {list_comprehension}")

# Instead of using a list comprehension we can use the map function to do the same thing.
map_function = map(divide_by_seven,(24,654,3,961,21))

# Print the results
print(f"An example of a map function: {list(map_function)}")

# 4. Demonstrate how to implement the previous example as a lambda function within the map function
map_function = map(lambda x: round(x/7,3),(24,654,3,961,21))
print(f"An example of a using the lambda function: {list(map_function)}")

# 5. Use the filter and lambda functions to get only the numbers divided by 3.
numbers = [12, 7, 9, 18, 25, 36, 42, 55, 63]
divisible_by_3 = list(filter(lambda x: x % 3 == 0, numbers))
print(divisible_by_3)
