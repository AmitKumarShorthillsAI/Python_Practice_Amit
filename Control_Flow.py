class ControlFlowExamples:
    def __init__(self):
        pass
    
    # If-elif-else statements
    def conditional_logic(self, value):
        if value > 10:
            print("Value is greater than 10")
        elif value == 10:
            print("Value is exactly 10")
        else:
            print("Value is less than 10")
    
    # Truthy vs Falsey values
    def truthy_vs_falsey(self, value):
        if value:
            print(f"{value} is Truthy")
        else:
            print(f"{value} is Falsey")
    
    # Ternary Operator
    def ternary_operator(self, a, b):
        min_value = a if a < b else b
        print(f"The smaller value is: {min_value}")
    
    # Short Circuiting in logical operators
    def short_circuiting(self, a, b):
        result = a or b  # If a is truthy, b is not evaluated
        print(f"Short circuit OR result: {result}")
        result = a and b  # If a is falsey, b is not evaluated
        print(f"Short circuit AND result: {result}")
    
    # Logical Operators
    def logical_operators(self, a, b):
        print(f"a AND b: {a and b}")
        print(f"a OR b: {a or b}")
        print(f"NOT a: {not a}")
    
    # 'is' vs '=='
    def is_vs_equals(self, a, b):
        print(f"a == b: {a == b}")  # Value comparison
        print(f"a is b: {a is b}")  # Identity comparison
    
    # For Loop
    def for_loops(self, iterable):
        for item in iterable:
            print(f"Item: {item}")
    
    # Iterables
    def count_iterables(self, iterable):
        print(f"Number of elements: {len(iterable)}")
    
    # range()
    def use_range(self, start, stop, step=1):
        for i in range(start, stop, step):
            print(i, end=' ')
        print()
    
    # enumerate()
    def use_enumerate(self, iterable):
        for index, item in enumerate(iterable):
            print(f"Index {index}: {item}")
    
    # While Loop
    def while_loops(self, limit):
        count = 0
        while count < limit:
            print(f"Count: {count}")
            count += 1
    
    # break, continue, pass
    def loop_control_statements(self):
        print("Break Example:")
        for i in range(5):
            if i == 3:
                break
            print(i)
        
        print("Continue Example:")
        for i in range(5):
            if i == 3:
                continue
            print(i)
        
        print("Pass Example:")
        for i in range(5):
            if i == 3:
                pass  # Placeholder for future logic
            print(i)
    
    # match Statements (Python 3.10+)
    def match_statements(self, value):
        match value:
            case 1:
                print("Value is 1")
            case 2:
                print("Value is 2")
            case _:
                print("Value is something else")
    
    # Function with Default Argument
    def greet(self, name="User"):
        print(f"Hello, {name}!")
    
    # Function with Keyword Arguments
    def display_info(self, name, age):
        print(f"Name: {name}, Age: {age}")
    
    # Function with Arbitrary Arguments
    def sum_numbers(self, *numbers):
        print(f"Sum: {sum(numbers)}")
    
    # Function with Unpacking Argument Lists
    def multiply(self, a, b):
        print(f"Product: {a * b}")
    
    def unpack_arguments(self, args):
        self.multiply(*args)
    
    # Lambda Expression
    def lambda_expression(self, x, y):
        add = lambda a, b: a + b
        print(f"Lambda sum: {add(x, y)}")
    
    # Function Documentation Strings
    def documented_function(self):
        """This function demonstrates docstrings."""
        print("This function has a docstring!")
    
    # Function Annotations
    def annotated_function(self, x: "A value", y: int) -> int:
        return x + y
    def myfunction(self, a: "physics", b:"Maths" = 20) -> int:
        return a + b

# Execution
if __name__ == "__main__":
    example = ControlFlowExamples()
    
    print("\nConditional Logic:")
    example.conditional_logic(10)
    
    print("\nTruthy vs Falsey:")
    example.truthy_vs_falsey("")
    example.truthy_vs_falsey("Hello")
    
    print("\nTernary Operator:")
    example.ternary_operator(5, 10)
    
    print("\nShort Circuiting:")
    example.short_circuiting(False, "Evaluated")
    
    print("\nLogical Operators:")
    example.logical_operators(True, False)
    
    print("\n'is' vs '==':")
    example.is_vs_equals([1, 2, 3], [1, 2, 3])
    
    print("\nFor Loops:")
    example.for_loops(["apple", "banana", "cherry"])
    
    print("\nIterables:")
    example.count_iterables([1, 2, 3, 4])
    
    print("\nUsing range():")
    example.use_range(1, 10, 2)
    
    print("\nUsing enumerate():")
    example.use_enumerate(["Python", "Java", "C++"])
    
    print("\nWhile Loops:")
    example.while_loops(3)
    
    print("\nLoop Control Statements:")
    example.loop_control_statements()
    
    print("\nMatch Statements:")
    example.match_statements(2)
    
    print("\nDefining Functions:")
    example.greet("Amit")
    example.display_info(name="Amit", age=25)
    
    print("\nArbitrary Arguments:")
    example.sum_numbers(1, 2, 3, 4)
    
    print("\nUnpacking Arguments:")
    example.unpack_arguments((3, 4))
    
    print("\nLambda Expression:")
    example.lambda_expression(10, 20)
    
    print("\nDocumented Function:")
    example.documented_function()
    
    print("\nFunction Annotations:")
    print("Annotated Sum:", example.annotated_function(5, 7))
    print("Function Annotation:", example.annotated_function.__annotations__)
    print("MyFunction's annoted sum:", example.myfunction(10))
    print("MyFunction's annotation:", example.myfunction.__annotations__)