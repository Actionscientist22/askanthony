"""Creating a Car class with methods and instances"""

# Define the Car class
class Car:
    """Creating a Car class with parameters and methods"""
    def __init__(self, make, model, body, engine, year, color):
        self.make = make
        self.model = model
        self.body = body
        self.engine = engine
        self.year = year
        self.color = color

    # Create a method to get the make of the car
    def get_make(self):
        """Returns the make of the car"""
        return self.make

    # Create a method to get the model of the car
    def get_model(self):
        """Returns the model of the car"""
        return self.model

    # Create a method to get the body of the car
    def get_body(self):
        """Returns the body of the car"""
        return self.body

    # Create a method to get the engine of the car
    def get_engine(self):
        """Returns the engine of the car"""
        return self.engine

    # Create a method to get the year of the car
    def get_year(self):
        """Returns the year of the car"""
        return self.year

    # Create a method to get the color of the car
    def get_color(self):
        """Returns the color of the car"""
        return self.color

    # Create three setter methods to change three parameters of the `Car` class.
    # YOUR SETTER METHODS GO HERE




# Create an instance of the Car class
# Use the following default information or create your own default data.
car = Car("Subaru", "CrossTrek Limited", "SUV", "2.5L, 4 cylinder","2020", "Pearl Blue")

# Get the current information on the car.
print('Here are the details of the car.')
print(f"Make: {car.get_make()}")
print(f"Model: {car.get_model()}")
print(f"Body: {car.get_body()}")
print(f"Engine Type: {car.get_engine()}")
print(f"Year made: {car.get_year()}")
print(f"Color: {car.get_color()}")

# Prompt the user to change the three parameters for the car.
# Hint create new variables for each prompt.


# Pass the updated car information from the user to the setter method you created above.


# Print the updated information of the car.
print('Here are the updated details of the car.')
print(f"Make: {car.get_make()}")
print(f"Model: {car.get_model()}")
print(f"Body: {car.get_body()}")
print(f"Engine Type: {car.get_engine()}")
print(f"Year made: {car.get_year()}")
print(f"Color: {car.get_color()}")
