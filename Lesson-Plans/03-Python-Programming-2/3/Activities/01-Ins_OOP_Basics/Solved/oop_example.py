#define a car class

class Car:
    """Creating the car class
    """
    def __init__(self,make, model):
        self.make=make
        self.model=model
        
my_car=Car("GMC","Sierra")

print(f"Make:{my_car.make}")