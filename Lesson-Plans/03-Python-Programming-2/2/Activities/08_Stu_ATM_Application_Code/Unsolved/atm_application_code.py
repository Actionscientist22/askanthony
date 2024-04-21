"""This is a basic ATM Application.
This is a program consists of the basic actions of an ATM.
"""

accounts = [
    {
    "pin": 123456,
    "balance" : 1436.19},
    {
    "pin" : 246802,
    "balance": 3571.87},
    {
    "pin": 135791,
    "balance" : 543.79},
    {
    "pin" : 123987,
    "balance": 25.89},
    {
    "pin" : 269731,
    "balance": 3278.42}
]

# Define the `login` function for the ATM application.
def login(pin):
    """The function a for loop to check to validate the PIN against this list of `accounts`.
        If the PIN is validated, the function should return the account's balance.
    Args:
        pin (integer): The users pin number

    Returns:
        If the pin matches one of the pin numbers in the "accounts"
        the account balance is returned.
    """
    for account in accounts:
        if int(pin) == account["pin"]:
            account_balance = account['balance']

    return account_balance


# Define the `check_balance` function for the ATM application.
def check_balance():
    """The function uses the account balance as a parameter.
    and returns the balance of the account.

    Args:
        account_balance (float): The balance of the account.

    Returns:
        Prints the account balance formatted to two decimal places and thousandths.
    """
    ## YOUR CODE HERE

# Define the `make_deposit` function for the ATM application.
def make_deposit():
    """# This function takes in the account balance and deposit amount as parameters.
    Then validates that the deposit amount is greater than 0.

    Args:
        account_balance (float): The balance of the account
        deposit (float): An amount deposited into the account greater than 0.

    Returns:
        The function returns the balance after being adjusted for the deposit.

    Notes:
        The deposit balance should equal the account balance plus the deposit amount.
    """
    ## YOUR CODE HERE
