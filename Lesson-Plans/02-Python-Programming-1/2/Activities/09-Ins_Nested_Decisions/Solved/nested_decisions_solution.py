# Nested if-else statements

issue_currency = "EUR"
price = 30.0

# Check if price is not negative (greater than equal to 0)
if price >= 0:
    # If price is not negative and currency is 'USD' (Dollar).
    if issue_currency == "USD":
        print("The currency is $", price)
    # If price is not negative and currency is 'EUR' (Euro).
    elif issue_currency == "EUR":
        print("The currency is €", price)
    # If anything other than the above.
    else:
        print("The currency is not in USD or EUR.")
# Else price is negative
else:
    print("Error, the price listed is a negative number")


# Nested loops

# Keep looping until we exit the loop
while True:

    # Declare user_number
    user_number = ""

    # Keep looping while user_number is not an integer
    while type(user_number) is not int:
        # Ask the user how many numbers to loop through
        user_number = input("How many numbers? ")

        # Validate the input is a number
        if user_number.isdigit():
            user_number = int(user_number)
        else:
            print("You didn't input a valid number")

    # Loop through the numbers. (Be sure to cast the string into an integer.)
    for x in range(user_number):

        # Print each number in the range
        print(x)

        # Limit the range to 20
        if x >= 20:
            print("Your input number is too high, breaking loop.")
            break


    # Once complete, ask the user if they want to quit
    user_play = input("Type 'q' to exit and anything else to continue. ")
    if user_play == 'q':
        break
