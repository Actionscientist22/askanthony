# Car Loan Calculator

In this activity, you'll practice working with Python functions.

## Background

Ever since you figured out how to calculate the total cost of the loan for your new car, all of your friends have been asking you to do their calculations.

It makes sense to put the future calculation in a function; this way, you only have to write the function once and then call it over and over.

Use the instructions and the starter file to create a `calculate_future_value` function and call it using the following `new_car_loan` dictionary:

```python
new_car_loan = {
    "current_loan_value" : 25000,
    "months_remaining" : 6,
    "annual_interest_rate" : 0.085,
    }
```

## Instructions

Open the [car_loan_calculator.py](Unsolved/car_loan_calculator.py) file and complete the following steps.

* Use the following future value formula for reference:

    ```python
    future_value = current_loan_value * (1 + (annual_interest_rate)) ** months_remaining
    ```

* Create a function called `calculate_future_value` that fulfills the following criteria:

    * The function should take in three arguments: `current_loan_value`, `annual_interest_rate`, and `months_remaining`.

    * The function body should contain the `future_value` formula.

    * The function should print the `future_value` to 2 decimal places and thousandths.

* Call the `calculate_future_value` function, passing the relevant information from the `new_car_loan` dictionary as parameters.

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
