"""This is a basic ATM Application.
"""

# Import the dependencies.
import sys
# Import the load_accounts and validate_pin functions from the utils file.
from utils import load_accounts, validate_pin
# Import the make_deposit function from the make_deposit file.
from actions.make_deposit import make_deposit
# Import the make_withdrawal function from the make_withdrawal file.
from actions.make_withdrawal import make_withdrawal


def main_menu():
    """Dialog for the ATM Main Menu."""

    # Determines action taken by application.
    action = input("Would you like to check your balance (b), make a deposit (d) or make a withdrawal (w)? Enter b, d, or w. \n")
    return action


def login():
    """This function uses a for loop to check to validate the PIN against this list of `accounts`.
        If the PIN is validated, the function should return the account's balance.
    Args:
        pin (integer): The users pin number

    Returns:
        If the pin matches one of the pin numbers in the "accounts"
        the account is returned.
    """
    # Calls validate_pin() function to confirm length.
    pin = input("Please enter your pin:\n")
    if not validate_pin(pin):
        sys.exit("Sorry, your account PIN is not valid. It must be 6 digits in length.")

    # If pin validates, calls load_accounts() and then verifies pin against accounts list. Returns account that matches pin.
    accounts = load_accounts()

    for account in accounts:
        if int(pin) == account["pin"]:
            return account
        # If no account was returned above, exit with an error

    sys.exit(
        "Sorry, your login was not successful. Your PIN does not link to an account. Please check your PIN and try again."
    )


def run():
    """This function starts the login process.
    It calls the login function and assigns the verified account to the account variable.
    Then, it calls the main_menU() function and ask the user what they want to do.
    A conditional statement is sued to process the action
    and calls the appropriate function based on the action.

    Returns:
        The adjusted balance after the action.

    """
    # Initiates login process. If pin verified, returns validated account.
    account = login()

    # Initiates ATM action: check balance, deposit or withdrawal.
    action = main_menu()

    # Processes the chosen action
    if action == "b":
        sys.exit(f"Your current account balance is {account['balance']}")
    elif action == "d":
        account = make_deposit(account)
    elif action == "w":
        account = make_withdrawal(account)

    # Prints the adjusted balance.
    print(
        f"Thank you for using this ATM. Your adjusted balance is ${account['balance']: ,.2f}."
    )


if __name__ == "__main__":
    # Call the run function.
    run()
