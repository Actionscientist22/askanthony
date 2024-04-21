"""Adjusts account balance after a deposit."""

import sys


def make_deposit(account):
    """This function prompts the user to make a deposit.
    If the amount is greater than 0.0 the balance was successful.
    If the amount is less than 0.0 then the system ask the user to try again.

    Args:
        account (dict): The keys and values of the validated account.

    Returns:
        account (dict): The account balance after the deposit.
    """
    # Use input to determine the amount of the deposit
    # Re-type amount from a string to a floating point number.
