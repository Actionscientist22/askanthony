def validate_pin(pin):
    """This function takes in the pin given by the user
    and checks to make sure its length is 6.

    Args:
        pin (integer): The pin for the account.

    Returns:
        If the pin is correct, the login function loads the account.
        If the pin is incorrect, the system lets the user know that the pin is incorrect.
    """
    # Verifies length of pin is 6 digits prints validations message and return True.
    # Else returns False.
    if len(pin) == 6:
        print("Your PIN is valid")
        return True
    else:
        return False

def load_accounts():
    """This function opens the CSV file. And appends each account: the pin and balance,
    to the accounts lists.

    Returns:
        accounts (dict object): A dictionary of all the accounts.
    """
    csvpath = Path('data/accounts.csv')
    accounts = []
    # Open and read the CSV file.
    with open(csvpath, newline='', encoding='utf-8') as csvfile:
        #  Get the rows of the CSV file.
        rows = csv.reader(csvfile)
        # Skip reading the header row.
        header = next(rows)
        for row in rows:
            pin = int(row[0])
            balance = float(row[1])
            account = {
                "pin": pin,
                "balance": balance
            }
            accounts.append(account)
        return accounts