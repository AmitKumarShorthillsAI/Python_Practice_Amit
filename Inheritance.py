# ________________________________________Single Inheritance____________________________________
# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name  # Instance attribute

    def make_sound(self):
        print(f"{self.name} makes a sound.")

# Child Class (inherits from Animal)
class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} barks.")  # Overriding the parent method

# Creating an object of Dog
dog = Dog("Bruno")
dog.make_sound()  # Output: Bruno barks.

# _________________________________________Multilevel Inheritance____________________________________
# Grandparent Class
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print(f"Vehicle Brand: {self.brand}")

# Parent Class (inherits from Vehicle)
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)  # Calling the parent constructor
        self.model = model

    def show_model(self):
        print(f"Car Model: {self.model}")

# Child Class (inherits from Car)
class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)  # Calling the parent constructor
        self.battery_capacity = battery_capacity

    def show_battery(self):
        print(f"Battery Capacity: {self.battery_capacity} kWh")

# Creating an object of ElectricCar
tesla = ElectricCar("Tesla", "Model 3", 75)
tesla.show_brand()   # Output: Vehicle Brand: Tesla (from Vehicle class)
tesla.show_model()   # Output: Car Model: Model 3 (from Car class)
tesla.show_battery() # Output: Battery Capacity: 75 kWh (from ElectricCar class)

# _________________________________________Multiple Inheritance____________________________________
# Parent Class 1
class Engine:
    def engine_type(self):
        print("This is a V8 engine.")

# Parent Class 2
class Wheels:
    def wheel_count(self):
        print("This vehicle has 4 wheels.")

# Child Class (inherits from Engine and Wheels)
class Car(Engine, Wheels):
    def car_info(self):
        print("This is a sports car.")

# Creating an object of Car
sports_car = Car()
sports_car.engine_type()  # Output: This is a V8 engine. (from Engine class)
sports_car.wheel_count()  # Output: This vehicle has 4 wheels. (from Wheels class)
sports_car.car_info()     # Output: This is a sports car. (from Car class)
