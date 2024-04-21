"""Adjusts account balance after a withdrawal"""

import sys


def make_withdrawal(account):
    """This function prompts the user to make a withdrawal.
    If the amount is less than or equal to 0.0 the withdrawal the system ask the user to try again.
    If the amount is less than or equal to the account balance the withdrawal was successful.
    Else the the withdrawal can't be made, and the system ask the user to try again.

    Args:
        account (dict): The keys and values of the validated account.

    Returns:
        account (dict): The account balance after the withdrawal.
    """
    # Use input to determine the amount of the withdrawal
    # Re-type amount from a string to a floating point number.
