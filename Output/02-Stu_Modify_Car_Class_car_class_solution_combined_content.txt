""" Creating a Car class with parameters and instances"""

# Define the Car class
class Car:
    """Creating a Car class with 6 parameters and instances"""
    def __init__(self, make, model, body, engine, year, color):
        self.make = make
        self.model = model
        self.body = body
        self.engine = engine
        self.year = year
        self.color = color

# Prompt the user to enter the information for the car for each parameter.
make = input("Enter the make of the car: ")
model = input("Enter the model of the car: ")
body = input("Enter the body type for the car: ")
engine = input("Enter the engine type for the car: ")
year = int(input("Enter the year the car was made: "))
color = input("Enter the color of the car: ")

# Create an instance of the `Car` class and pass in the variables from the user.
car = Car(make, model, body, engine, year, color)

# Print the details of the car
print('Here is the information you enter for the car.')
print(f"Make: {car.make}")
print(f"Model: {car.model}")
print(f"Body: {car.body}")
print(f"Engine Type: {car.engine}")
print(f"Year made: {car.year}")
print(f"Color: {car.color}")
