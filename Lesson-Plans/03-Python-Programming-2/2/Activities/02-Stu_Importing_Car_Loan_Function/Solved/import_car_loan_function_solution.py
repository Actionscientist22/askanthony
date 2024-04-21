# Import the calculate_future_value function from the CarLoan file.
from CarLoan import calculate_future_value

# Create the new_car_loan dictionary.
new_car_loan = {
    "current_loan_value": 25000,
    "months_remaining": 12,
    "annual_interest_rate": 0.0315
    }

# Set the function call equal to a variable called car_value.
# Pass the relevant information from the dictionary as parameters to the function call.
car_value = calculate_future_value(
    new_car_loan["current_loan_value"],
    new_car_loan["annual_interest_rate"],
    new_car_loan["months_remaining"]
    )

# Print the future value of the car to 2 decimal places.
print(f"The future value of the car is ${car_value: ,.2f}.")
