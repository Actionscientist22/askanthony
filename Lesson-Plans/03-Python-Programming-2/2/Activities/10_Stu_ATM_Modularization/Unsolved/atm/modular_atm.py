"""This is a basic ATM Application.

This is a program consists of the basic actions of an ATM.

Example:
    $ python app.py
"""
# Import the dependencies.
import csv
import sys
from pathlib import Path

from utils import (load_accounts,validate_pin)
# import utils
from actions.make_deposit import make_deposit
from actions.make_withdrawal import make_withdrawal






def main_menu():
    """This function prompts the user to make a selection check their balance,
    make a deposit, or make a withdrawal.

    Returns:
        The action that user wants to do.
    """
    # Determines action taken by application.
    action = input("Would you like to: \n"
                "Check your balance (b),\n"
                "Make a deposit (d),\n"
                "Or make a withdrawal (w)?|n"
                "Enter b, d, or w. \n")
    return action


def login():
    """This function uses ask the user to enter their pin number.
    The pin number is passed to the validate_pin function.
    If the pin is valid, then the load_accounts function is called and
    the dictionary of accounts is assigned the accounts variable.
    A for loop verifies the pin against the listed accounts.

    Returns:
        The pin and balance of the account after the pin is validated.
    """
    # Calls validate_pin() function to confirm length.
    pin = input("Please enter your pin:\n")
    if not validate_pin(pin):
        sys.exit("Sorry, your account PIN is not valid. It must be 6 digits in length.")

    # If pin validates, calls load_accounts() and then verifies pin against accounts list.
    # Returns account that matches pin.
    accounts = load_accounts()

    for account in accounts:
        if int(pin) == account["pin"]:
            return account
        # If no account was returned above, exit with an error

    sys.exit(
        "Sorry, your login was not successful. Please check your PIN and try again."
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
