""" Returning Values Demonstration"""

def average_numbers(numbers):
    """ Calculates the average of an array of numbers"""
    average = sum(numbers) / len(numbers)
    print("The average is: ", average)

if __name__ == "__main__":
    average_numbers([1, 2, 3])


# We can return values from inside a function and use those in other parts of the code.
def average_numbers(numbers):
    """ Calculates the average of an array of numbers"""
    average = sum(numbers) / len(numbers)
    return average

if __name__ == "__main__":
    first_average = average_numbers([1, 2, 3])
    second_average = average_numbers([4, 5, 6])
    print(f'The average of the first list is {first_average}')
    print(f'The average of the second list is {second_average}')
