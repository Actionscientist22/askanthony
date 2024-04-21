"""Pizza Order"""

def create_pizza_order():
    """
    The function prompts the user to choose three toppings
    from a list of five toppings and creates a pizza order.
    Args:
        None
    Returns:
        None. But it prints out the toppings on the pizza.
    Raises:
        ErrorType: If the user enters a number less than 1 or greater than 5
        then asks the user to try again.
    """
    # Create a list of toppings.
    toppings = ['pepperoni', 'mushrooms', 'onions', 'sausage', 'bell peppers']

    # Create a statement about the program.
    print("Welcome to the Sal's Famous Pizza!")
    print("Please choose three toppings for your pizza from the following options:")

    # Create a for loop the iterates through the toppings and displays them to the user.
    for i, topping in enumerate(toppings, start=1):
        print(f"{i}. {topping}")

    # Create an empty list for the toppings the user chooses.
    selected_toppings = []

    # Iterate through the a range of 3 for the number of toppings
    # Prompt the user to input a number for a topping.
    for _ in range(3):
        topping_number = int(input("Enter the number of your chosen topping: "))

        # Create a while loop that selects a number between 1 and 5.
        # If an number less than 1 or greater than 5 is select prompt the user to try again.
        while topping_number < 1 or topping_number > 5:
            print("Invalid topping number. Please try again.")
            topping_number = int(input("Enter the number of your chosen topping: "))

        # Retrieve the selected topping from the list using toppings[topping_number - 1]
        # Then add the topping to the list.
        selected_toppings.append(toppings[topping_number - 1])

    # Print out the order.
    print("Here is your order:")
    print("Your pizza comes with:", ", ".join(selected_toppings))

if __name__ == "__main__":
    # Call the function.
    create_pizza_order()
