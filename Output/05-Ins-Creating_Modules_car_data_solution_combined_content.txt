# Import the Car class from the car_data.py file.
from Car import Car

# Create an instance of the Car class.
car = Car("Subaru", "CrossTrek Limited", "SUV", "2.5L, 4 cylinder","2020", "Pearl Blue")

# Get the current make using the getter methods.
print('Here are the details of the car.')
print(f"Make: {car.get_make()}")
print(f"Model: {car.get_model()}")
print(f"Body: {car.get_body()}")
print(f"Engine Type: {car.get_engine()}")
print(f"Year made: {car.get_year()}")
print(f"Color: {car.get_color()}")

# Prompt the user to change three parameters for the car.
model = input("What Subaru model would you like? ")
year = int(input("What model year are you looking for? "))
color = input("What color would you like? ")


# Use the setter methods to change the information
car.set_model(model)
car.set_year(year)
car.set_color(color)

# Print the new details about the car.
print('Here are the updated details of the car.')
print(f"Make: {car.get_make()}")
print(f"Model: {car.get_model()}")
print(f"Body: {car.get_body()}")
print(f"Engine Type: {car.get_engine()}")
print(f"Year made: {car.get_year()}")
print(f"Color: {car.get_color()}")
