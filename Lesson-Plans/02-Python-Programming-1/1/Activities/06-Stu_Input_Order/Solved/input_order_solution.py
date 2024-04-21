# Take input of an item the user wants to purchase
item = input("What is the item that you want to purchase? ")

# Ask how much the item costs and cast it as a number.
# What type of number should it be cast as?
item_cost = float(input("How much does " + item + " cost? "))

# Ask what quantity of the item should be purchased and cast it as a number.
# What type of number should it be cast as?
item_quantity = int(
    input("What quantity of " + item + " would you like to " + "purchase? ")
)

# Print the item cost along with its data type
print("The data type of " + str(item_cost) + " is " + str(type(item_cost)))

# Print the item quantity along with its data type
print("The data type of " + str(item_quantity) + " is " + str(type(item_quantity)))

# Print results
print(
    "You want to buy "
    + str(item_quantity)
    + " "
    + item
    + "s for "
    + str(item_cost)
    + " each."
)
