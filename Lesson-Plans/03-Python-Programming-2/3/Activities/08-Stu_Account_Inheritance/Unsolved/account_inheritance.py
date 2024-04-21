# Import the SavingsAccount and CD classes from the Accounts.py file.
# ADD YOUR CODE HERE

# Prompt the user to set the savings balance and interest rate.
# ADD YOUR CODE HERE

# Create an instance of the `SavingsAccount` class that sets the users savings account balance and interest.
# ADD YOUR CODE HERE
# savings_data =

# Prompt the user to set the CD balance, interest rate, and months for the CD.
# ADD YOUR CODE HERE

# Create an instance of the `CD` class that sets the users cd account balance, interest, and length of months.
# ADD YOUR CODE HERE
# cd_data =

# Display the savings account data.
print('Here are the details of the savings account.')
print("The balance is: $", format(savings_data.get_balance(), ',.2f'))
print("APR Interest Rate is: ", format(savings_data.get_interest(), ',.2f'),"%")

# Display the CD account data.
print('Here are the details of the CD account.')
print("The balance is: $", format(cd_data.get_balance(), ',.2f'))
print("APR Interest Rate is:", format(cd_data.get_interest(), ',.2f'),'%')
print(f"Length of CD is: {cd_data.get_months()} months.")
