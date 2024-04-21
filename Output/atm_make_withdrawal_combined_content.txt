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
    amount = input("How much would you like to withdraw?\n")
    amount = float(amount)

    # Validates amount of withdrawal. If less than or equal to 0 system exits with error message.
    if amount <= 0.0:
        sys.exit("This is not a valid withdrawal amount. Please try again.")

    # Validates if withdrawal amount is less than or equal to account balance, processes withdrawal and returns account.
    # Else system exits with error messages indicating that the account is short of funds.
    if amount <= account["balance"]:
        account["balance"] = account["balance"] - amount
        print("Your withdrawal was successful!")
        return account
    sys.exit(
            "You do not have enough money in your account to make this withdrawal. Please try again."
        )
