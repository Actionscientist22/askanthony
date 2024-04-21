# ATM Application Code

In this activity, you will write the business logic and code associated with three ATM functions.


## Instructions

Open [atm_application_code.py](Unsolved/atm_application_code.py) in the Unsolved folder, design business logic and then write the code for the following ATM functions:

* Check the account balance.

* Make a deposit.

* Make a withdrawal.

Before you start to write any code, think through the business logic associated with each function. These should include any expected input parameters and the return value of the function, as well as account for any user input that will need to be validated by the application (such as validating that a PIN is the correct number of digits.

Once your business logic is in place, write the associated code for each function.

Use the following business logic and code associated with the `login` function as an example.

```python
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
```

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
