"""Creating a Car class with methods and instances"""

# Define the Car class
class Car:
    """Creating a Car class with methods"""
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

    # Create a method to change the model of the car
    def set_model(self, new_model):
        """Sets the make of the car"""
        self.model = new_model

# Define the CarExtras class that inherits the attributes from the Car class.
class CarExtras(Car):
    """Creating a CarExtras class with methods"""
    def __init__(self, make, model, body, engine, year, color, anti_theft, alarm, tint, ext_warranty):
        # Call the parent class's __init__ method and pass the required arguments.
        Car.__init__(self, make, model, body, engine, year, color)

        # Initialize the attributes for the CarExtras class.
        self.anti_theft = anti_theft
        self.alarm = alarm
        self.tint = tint
        self.ext_warranty = ext_warranty

    def get_anti_theft(self):
        """Sets the antitheft for the car"""
        return self.anti_theft

    def get_alarm(self):
        """Sets the alarm for the car"""
        return self.alarm

    def get_tint(self):
        """Sets the tint for the car"""
        return self.tint

    def get_ext_warranty(self):
        """Sets the extended warranty for the car"""
        return self.ext_warranty
