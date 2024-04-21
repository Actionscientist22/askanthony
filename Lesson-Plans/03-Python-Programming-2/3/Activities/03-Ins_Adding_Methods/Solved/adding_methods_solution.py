"""Creating a Car class with methods and instances"""

# Define the Car class
class Car:
    """Creating a Car class with methods"""
    def __init__(self, make, model): # add the model parameter
        self.make = make
        self.model = model

        # Create a method to get the make of the car
    def get_make(self):
        """Gets the make of the car"""
        return self.make

    # Create a method to change the make of the car
    def set_make(self, new_make):
        """Sets the make of the car"""
        self.make = new_make

    # Create a method to set the model of the car
    def set_model(self, new_model):
        """Sets the make of the car"""
        self.make = new_model

    # Create the get_model method
    def get_model(self, model):
        """Gets the model of the car"""
        return self.model



# Create an instance of the Car class.
my_car = Car("Toyota","Camry")

# Get the initial  make of the car.
initial_make = my_car.get_make()
print(f"Initial Make: {initial_make}")

# Set a new make
my_car.set_make("Honda")

# Get the updated make
updated_make = my_car.get_make()
print(f"Updated Make: {updated_make}")
