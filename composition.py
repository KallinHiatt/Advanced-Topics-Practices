#composition is a class that exsists inside of another class (class has a other class)

class Car:
    def __init__(self, make, model, year, engine):
        self.make = make
        self.model = model
        self.year = year
        self.engine = engine

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
    
    def __repr__(self):
        return f"Car({self.make}, {self.model}, {self.year}, {self.engine})"
#This basically is only needed for other programmers. It is for debugging purposes, and gives the class and all the attributes inside the class



class Engine:
    def __init__(self, configuration, displacement, horsepower, torque):
        self.configuration = configuration
        self.displacement = displacement
        self.horsepower = horsepower
        self.torque = torque
    def ignition(self):
        print("VROOM! VROOM!")
    def __repr__(self):
        return f"Car({self.configuration}, {self.displacement}, {self.horsepower}, {self.torque})"
    def __str__(self):
        return f"The engine is a {self.configuration} with {self.displacement}, {self.horsepower}, and {self.torque}"

my_engine = Engine("V8", 5.8, 326, 344)
my_car = Car("Mazda", "Mazda3", 2013, my_engine)
#to call a composit class you must access where it is saved within the class
print(my_car)

my_car.engine.ignition()
print(repr(my_car))
print(repr(my_engine))