# Declare lists
rides = []
prices = []

# Continuous loop
while True:
    # Keep adding rides until exiting loop
    rides.append(input("What ride should be added to the amusement park? "))

    # Continuous loop
    while True:
        # Prompt user for the cost of the ride
        cost = input("How much does it cost to ride this ride? ")

        # Check if the input is a number
        if cost.replace(".","",1).isdigit():
            # Check if the input is less than or equal to 15
            if float(cost) <= 15:
                # Convert the input to a float and append it to the prices list
                prices.append(float(cost))
                # Exit the loop
                break
            else:
                print("Please choose a price that is $15 or less.")
        else:
            print("You didn't input a valid price")

    # Ask the user if they wish to quit, and break the loop if they type 'q'
    keep_going = input("Type 'q' to exit and anything else to add another ride. ")
    if keep_going == 'q':
        break

# Loop through the rides and prices lists by finding the length of rides
for i in range(len(rides)):
    # Set the discount variable to False
    discount = False
    # Check if the price is greater than $5
    if prices[i] > 5:
        # Update the price to include a 10% discount
        prices[i] *= 0.9
        # Set the discount variable to true
        discount = True
    # Print the ride name and price, with the price formatted to 2 decimal places
    print(f"{rides[i]} costs ${prices[i]:.2f} to ride.")
    # If a discount was applied, print a message that says this
    if discount:
        print("A discount of 10% is applied.")

    # Print a dash 40 times
    print("-" * 40)