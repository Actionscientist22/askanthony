# ATM Modularization

In this activity, you will modularize the ATM application so that the codebase matches the following image:

```text
atm
├── actions
│   ├── make_deposit.py
│   └── make_withdrawal.py
├── data
│   └── accounts.csv
├── modular_atm.py
└── utils.py
```


## Instructions

Confirm that you're working inside the [atm](Unsolved/atm/) folder. Then complete the following steps:

1. Inside the [atm](Unsolved/atm/) folder, create a new folder called `actions`. Then, in the `actions` folder, create two new Python script files: `make_deposit.py` and `make_withdrawal.py`.

2. Copy the `make_deposit(account)` function from inside [modular_atm.py](Unsolved/atm/modular_atm.py) file to the `make_deposit.py` file. Once the function has been copied over, you can delete it from `modular_atm.py` file.

4. Inside the `make_deposit.py` file, import the Python library `sys`.

    ```python
    import sys
    ```

5. In `modular_atm.py`file, add the following import statement at the top:

    ```python
    # Import the make_deposit function from the make_deposit file.
    from actions.make_deposit import make_deposit
    ```

6. Repeat the previous three steps for the `make_withdrawal(account)` function.

    * Move it from `modular_atm.py` file and add it to the `make_withdrawal.py` file.
    * Inside the `make_withdrawal.py` file, import the Python library `sys`.
    * In `modular_atm.py`file, add the following import statement at the top:

        ```python
        # Import the make_withdrawal function from the make_withdrawal file.
        from actions.make_withdrawal import make_withdrawal
        ```

7. Inside the `atm` folder, create a Python file called `utils.py`.

8. Copy the `load_accounts()` and `validate_pin(pin)` functions from inside `modular_atm.py` file into the `utils.py` file. Once they've been copied over, they can be deleted from `modular_atm.py`.

9. At the top of the `utils.py` file add the following import statements:

    ```python
    # Import the dependencies.
    import csv
    import sys
    from pathlib import Path
    ```

10. Confirm that your new ATM application structure matches the figure above. If it does, run the `modular_atm.py` file to confirm that the ATM application works.


---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
