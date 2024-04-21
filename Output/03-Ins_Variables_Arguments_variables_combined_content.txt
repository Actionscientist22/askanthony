"""Passing Arguments."""

# Define a function that will add two numbers.
def add():
    """This function takes two numbers and adds them and then returns the total."""
    first_number = 1 # This is a local scope of the function.
    second_number = 2 # This is a local scope of the function.
    total = first_number + second_number
    print(f"Your total is: {total}")


if __name__ == "__main__":
    add()
    print(first_number)


# Global variables for first_number and second_number.
first_number = 2
second_number = 3

# Define a function that will add two numbers.
