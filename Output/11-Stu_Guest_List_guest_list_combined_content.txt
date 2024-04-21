# initialize list of guests for user input
guests = []

# Begin a continuous loop that should only be exited when the user says they're 
# done with entering guests.
while True:

    # Ask the user for the guest's name ans save it to a variable
    guest_name = input("Please enter the name of the guest. ")

    # Begin a continuous loop to ask for number of adult guests and check for 
    # input error. Exit the loop when the input is a number and that number 
    # is converted to an integer.
    while True:
        party_number_adults = input(f"How many adult guests in {guest_name}'s party? ")
        if party_number_adults.isdigit():
            party_number_adults = int(party_number_adults)
            break
        else:
            print("You didn't enter a valid response. Please enter a number.")

    # Begin a continuous loop to ask for number of children guests and check for 
    # input error. Exit the loop when the input is a number and that number 
    # is converted to an integer.
    while True:
        party_number_children = input(f"How many child guests in {guest_name}'s party? ")
        if party_number_children.isdigit():
            party_number_children = int(party_number_children)
            break
        else:
            print("You didn't enter a valid response. Please enter a number.")

    # Append the guest list with a dictionary that includes the guest name,
    # number of adults and number of children in the party
    guests.append({
        "guest_name": guest_name,
        "party_number_adults": party_number_adults,
        "party_number_children": party_number_children
    })

    more_guests = input("Do you have more guests to register? Type (n) to exit. ")
    if more_guests == 'n':
        break

# Print the guests dictionary to observe the structure
# Comment out the following line when it is no longer needed
print(guests)

# Use a list comprehension to create a list of tuples with the guests for each
# party of guests in the format (adults, children)


# Use a list comprehension to calculate the total number of adult guests


# Use a list comprehension to calculate the total number of child guests


# Use a list comprehension to calculate the total number of guests


# Bonus: Use a list comprehension to create a string of the guest's name in 
# title case and the total number of guests in the party

