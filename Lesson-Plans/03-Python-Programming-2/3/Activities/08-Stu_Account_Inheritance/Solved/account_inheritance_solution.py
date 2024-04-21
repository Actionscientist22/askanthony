# Import the SavingsAccount and CD classes from the Accounts.py file.
from Accounts import SavingsAccount, CD

# Prompt the user to set the savings balance and interest rate.
savings_balance = float(input('What is your savings account balance? '))
savings_interest = float(input('What is the APR for the savings account? '))

# Create an instance of the `SavingsAccount` class that sets the users savings account balance and interest.
savings_data = SavingsAccount(savings_balance, savings_interest)

# Prompt the user to set the CD balance, interest rate, and months for the CD.
cd_balance = float(input('What is your initial CD account balance? '))
cd_interest = float(input('What is the APR for the CD account? '))
cd_maturity = int(input('What is the length of months for your CD? '))

# Create an instance of the `CD` class that sets the users cd account balance, interest, and length of months.
cd_data = CD(cd_balance, cd_interest, cd_maturity)

# Display the savings account data.
print('Here are the details of the savings account.')
print("The balance is: $", format(savings_data.get_balance(), ',.2f'))
print("APR Interest Rate is: ", format(savings_data.get_interest(), ',.2f'),"%")

# Display the CD account data.
print('Here are the details of the CD account.')
print("The balance is: $", format(cd_data.get_balance(), ',.2f'))
print("APR Interest Rate is:", format(cd_data.get_interest(), ',.2f'),'%')
print(f"Length of CD is: {cd_data.get_months()} months.")
