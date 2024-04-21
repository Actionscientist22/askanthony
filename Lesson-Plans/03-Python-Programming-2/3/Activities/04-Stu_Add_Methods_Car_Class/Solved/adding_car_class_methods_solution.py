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

    # Create a method to change the make of the car
    def set_make(self, new_make):
        """Sets the make of the car"""
        self.make = new_make

    # Create a method to change the model of the car
    def set_model(self, new_model):
        """Sets the make of the car"""
        self.model = new_model

    # Create a method to change the body of the car
    def set_body(self, new_body):
        """Sets the make of the car"""
        self.body = new_body

    # Create a method to change the engine of the car
    def set_engine(self, new_engine):
        """Sets the make of the car"""
        self.engine = new_engine

    # Create a method to change the make of the car
    def set_year(self, new_year):
        """Sets the make of the car"""
        self.year = new_year

    # Create a method to change the color of the car
    def set_color(self, new_color):
        """Sets the make of the car"""
        self.color = new_color


# Create an instance of the Car class.
car = Car("Subaru", "CrossTrek Limited", "SUV", "2.5L, 4 cylinder","2020", "Pearl Blue")

# Get the current make
print('Here are the details of the car.')
print(f"Make: {car.get_make()}")
print(f"Model: {car.get_model()}")
print(f"Body: {car.get_body()}")
print(f"Engine Type: {car.get_engine()}")
print(f"Year made: {car.get_year()}")
print(f"Color: {car.get_color()}")

# Prompt the user to change three attributes of the car.
model = input("What Subaru model would you like? ")
year = int(input("What model year are you looking for? "))
color = input("What color would you like? ")


# Pass the updated car information from the user to the setter method you created above.
car.set_model(model)
car.set_year(year)
car.set_color(color)

# Print the updated information of the car.
print('Here are the updated details of the car.')
print(f"Make: {car.get_make()}")
print(f"Model: {car.get_model()}")
print(f"Body: {car.get_body()}")
print(f"Engine Type: {car.get_engine()}")
print(f"Year made: {car.get_year()}")
print(f"Color: {car.get_color()}")
