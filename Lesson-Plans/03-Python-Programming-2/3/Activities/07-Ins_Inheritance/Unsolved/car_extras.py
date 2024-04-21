# Import the Car and CarExtras classes from the CarData.py file.
from CarData import CarExtras

# Create an instance of the CarExtras class.
my_car = CarExtras("Toyota", "Camry", "Sedan", "2.5L", 2022, "Silver", "Yes", "Yes", "No", "No")

# Get the current make
print('Here are the details of the car.')
print(f"Make: {my_car.get_make()}")
print(f"Model: {my_car.get_model()}")
print(f"Body: {my_car.get_body()}")
print(f"Engine Type: {my_car.get_engine()}")
print(f"Year made: {my_car.get_year()}")
print(f"Color: {my_car.get_color()}")
print(f"Anti-Theft: {my_car.get_anti_theft()}")
print(f"Alarm: {my_car.get_alarm()}")
print(f"Tint: {my_car.get_tint()}")
print(f"Extended Warranty: {my_car.get_ext_warranty()}")
