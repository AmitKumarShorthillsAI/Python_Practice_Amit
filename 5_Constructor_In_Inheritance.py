# ______________________________Single Inheritance (Calling Parent Constructor with super())__________________________
# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal {self.name} is created.")

# Child Class (Calling parent constructor)
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Calls parent constructor
        self.breed = breed
        print(f"Dog of breed {self.breed} is created.")

# Creating object of Dog
dog1 = Dog("Bruno", "Labrador")


# ______________________________Single Inheritance (Calling Parent Constructor without super())__________________________
# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal {self.name} is created.")

# Child Class (Calling parent constructor)
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name)  # Calls parent constructor
        self.breed = breed
        print(f"Dog of breed {self.breed} is created.")


# _______________________________Multilevel Inheritance (Calling Parent Constructor with super())__________________________
# Grandparent Class
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        print(f"Vehicle Brand: {self.brand}")

# Parent Class
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)  # Calls Vehicle constructor
        self.model = model
        print(f"Car Model: {self.model}")

# Child Class
class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)  # Calls Car constructor
        self.battery_capacity = battery_capacity
        print(f"Battery Capacity: {self.battery_capacity} kWh")

# Creating an object of ElectricCar
tesla = ElectricCar("Tesla", "Model S", 100)


# _______________________________Multilevel Inheritance (Calling Parent Constructor without super())__________________________
# Grandparent Class
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        print(f"Vehicle Brand: {self.brand}")
# Parent Class
class Car(Vehicle):
    def __init__(self, brand, model):
        Vehicle.__init__(self, brand)  # Calls Vehicle constructor
        self.model = model
        print(f"Car Model: {self.model}")
# Child Class
class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        Car.__init__(self, brand, model)  # Calls Car constructor
        self.battery_capacity = battery_capacity
        print(f"Battery Capacity: {self.battery_capacity} kWh")
# Creating an object of ElectricCar
tesla = ElectricCar("Tesla", "Model S", 100)


# _______________________________Multiple Inheritance (Diamond Problem & super() with MRO)__________________________
# Parent Class 1
class A:
    def __init__(self):
        print("Constructor of A")

# Parent Class 2
class B:
    def __init__(self):
        print("Constructor of B")

# Child Class (inherits from A & B)
class C(A, B):
    def __init__(self):
        super().__init__()  # Calls A's constructor (MRO decides order)
        print("Constructor of C")

# Creating an object of C
obj = C()


# _______________________________Multiple Inheritance (Diamond Problem without super())__________________________
# Parent Class 1
class A:
    def __init__(self):
        print("Constructor of A")
# Parent Class 2
class B:
    def __init__(self):
        print("Constructor of B")
# Child Class (inherits from A & B)
class C(A, B):
    def __init__(self):
        A.__init__(self)  # Calls A's constructor
        B.__init__(self)  # Calls B's constructor
        print("Constructor of C")
# Creating an object of C
obj = C()
# Output:
# Constructor of A
# Constructor of B
# Constructor of C
# This can lead to multiple calls to parent constructors, which is not efficient.

# _______________________________Using cooperative multiple inheritance__________________________________________
class A:
    def __init__(self):
        super().__init__()  # Calls next class in MRO
        print("Constructor of A")

class B:
    def __init__(self):
        super().__init__()
        print("Constructor of B")

class C(A, B):
    def __init__(self):
        super().__init__()
        print("Constructor of C")

obj = C()
# Output:
# Constructor of B
# Constructor of A
# Constructor of C
# This ensures that each constructor is called only once in the order defined by the MRO.
# In this example, the MRO ensures that the constructors of both A and B are called before C's constructor.


# _______________________________Calling Other Parent Methods with super()__________________________
class Parent:
    def show(self):
        print("Parent method called")

class Child(Parent):
    def show(self):
        super().show()  # Calls Parent's show() method
        print("Child method called")

# Creating object
obj = Child()
obj.show()
# Output:
# Parent method called
# Child method called
# This demonstrates how to call a method from the parent class using super() within the child class.


# _______________________________Calling Other Parent Methods without super()__________________________
class Parent:
    def show(self):
        print("Parent method called")
class Child(Parent):
    def show(self):
        Parent.show(self)  # Calls Parent's show() method
        print("Child method called")
# Creating object
obj = Child()
obj.show()
# Output:
# Parent method called
# Child method called
# This demonstrates how to call a method from the parent class without using super() within the child class.