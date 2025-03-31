# __________________________________Method Overriding (Runtime Polymorphism)____________________
# Parent class
class Animal:
    def make_sound(self):
        print("Animal makes a sound.")

# Child class overriding method
class Dog(Animal):
    def make_sound(self):
        print("Dog barks.")

class Cat(Animal):
    def make_sound(self):
        print("Cat meows.")

# Creating objects
dog = Dog()
cat = Cat()

# Calling overridden methods
dog.make_sound()  # Output: Dog barks.
cat.make_sound()  # Output: Cat meows.


# ________________________________Method Overloading (Compile-time Polymorphism)____________________
# (a) Method Overloading using default arguments
class MathOperations:
    def add(self, a, b=0, c=0):
        return a + b + c

# Creating object
math_op = MathOperations()

# Different ways to call add() method
print(math_op.add(5))         # Output: 5
print(math_op.add(5, 10))     # Output: 15
print(math_op.add(5, 10, 15)) # Output: 30


# (b) Method Overloading using variable-length arguments
class MathOperationsVarArgs:
    def add(self, *args):
        return sum(args)
# Creating object
math_op_var = MathOperationsVarArgs()
# Different ways to call add() method
print(math_op_var.add(5))               # Output: 5
print(math_op_var.add(5, 10))           # Output: 15
print(math_op_var.add(5, 10, 15))       # Output: 30
print(math_op_var.add(5, 10, 15, 20))   # Output: 50

# (c) Method Overloading using @dispatch decorator
from multipledispatch import dispatch # pip install multipledispatch

class MathOperations:
    @dispatch(int, int)
    def add(self, a, b):
        return a + b

    @dispatch(int, int, int)
    def add(self, a, b, c):
        return a + b + c

# Creating object
math_op = MathOperations()

print(math_op.add(5, 10))     # Output: 15
print(math_op.add(5, 10, 15)) # Output: 30


# There are several ways to achieve method overloading in Python, including:
# 1. Using default arguments
# 2. Using variable-length arguments (*args)
# 3. Using the @dispatch decorator from the multipledispatch library
# 4. Using if-else conditions to check argument types
# 5. Using class methods or static methods to create overloaded methods
# 6. Using lambda functions for simple overloads
# 7. Using separate methods with different names for different argument types
# 8. Using the @overload decorator from the typing module etc.


# ________________________________Operator Overloading____________________________________
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading the '+' operator
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def display(self):
        print(f"Point({self.x}, {self.y})")

# Creating objects
p1 = Point(3, 4)
p2 = Point(1, 2)

# Adding two objects using overloaded '+'
p3 = p1 + p2
p3.display()  # Output: Point(4, 6)


# ________________________________Duck typing________________________________________
class Bird:
    def fly(self):
        print("Bird is flying.")

class Airplane:
    def fly(self):
        print("Airplane is flying.")

class Fish:
    def swim(self):
        print("Fish is swimming.")

# Function that accepts any object with 'fly' method
def lift_off(entity):
    entity.fly()

# Creating objects
bird = Bird()
plane = Airplane()
fish = Fish()

# Works for any class that has a 'fly' method
lift_off(bird)  # Output: Bird is flying.
lift_off(plane) # Output: Airplane is flying.
# lift_off(fish)  # ❌ This will raise an AttributeError
