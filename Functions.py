class BasicFunctionConcepts:
    """Defining and calling functions, passing arguments, returning values."""
    
    def basic_function(self):
        """A simple function without parameters."""
        print("Hello from a function!")
    
    def function_with_args(self, name, age):
        """Function with positional arguments."""
        print(f"Name: {name}, Age: {age}")
    
    def function_with_defaults(self, name="John", age=30):
        """Function with default argument values."""
        print(f"Default Name: {name}, Default Age: {age}")
    
    def function_with_kwargs(self, **kwargs):
        """Function using **kwargs."""
        print("Keyword Arguments:", kwargs)
    
    def function_with_args_kwargs(self, *args, **kwargs):
        """Function using *args and **kwargs."""
        print("Positional Arguments:", args)
        print("Keyword Arguments:", kwargs)
    
    def function_return_values(self, x, y):
        """Function returning values."""
        return x + y, x - y  # Returning multiple values


class ScopeOfVariables:
    """Understanding local and global variables."""
    
    global_var = "I am global"
    
    def local_scope_example(self):
        """Function demonstrating local variable scope."""
        local_var = "I am local"
        print(local_var)
    
    def global_scope_example(self):
        """Function demonstrating global variable access."""
        print(self.global_var)
    
    def modify_global_variable(self):
        """Using global keyword to modify global variable."""
        global global_var
        global_var = "Modified global variable"
        print(global_var)


class BuiltInAndUserFunctions:
    """Examples of built-in and user-defined functions."""
    
    def built_in_examples(self):
        """Demonstrating common built-in functions."""
        print("Length:", len("Hello"))
        print("Type:", type(10))
        print("Range:", list(range(5)))
    
    def user_defined_function(self, x):
        """Example of a user-defined function."""
        return x ** 2


class RecursionExample:
    """Understanding recursion with base case and recursive step."""
    
    def factorial(self, n):
        """Recursive function for factorial calculation."""
        if n == 0:
            return 1
        return n * self.factorial(n - 1)


class AdvancedFunctionTopics:
    """Exploring lambda functions, higher-order functions, and decorators."""
    
    def lambda_example(self):
        """Using lambda function for simple calculations."""
        square = lambda x: x ** 2
        print("Lambda Square:", square(5))
    
    def higher_order_function(self, func, value):
        """Function that takes another function as an argument."""
        return func(value)
    
    def decorator_example(self, func):
        """Simple function decorator."""
        def wrapper():
            print("Executing function...")
            func()
            print("Execution finished.")
        return wrapper


class GeneratorsAndComposition:
    """Using generators and function composition."""
    
    def simple_generator(self, n):
        """A generator function yielding values."""
        for i in range(n):
            yield i
    
    def compose_functions(self, f, g, x):
        """Function composition: Applying g, then f."""
        return f(g(x))


class MetaclassesAndPartialFunctions:
    """Understanding metaclasses and partial functions."""
    
    def metaclass_example():
        """Simple metaclass example."""
        class Meta(type):
            def __new__(cls, name, bases, attrs):
                attrs['created_by_meta'] = True
                return super().__new__(cls, name, bases, attrs)
        
        class MyClass(metaclass=Meta):
            pass
        
        obj = MyClass()
        print("Has meta attribute:", hasattr(obj, 'created_by_meta'))
    
    def partial_function_example(self):
        """Using functools.partial."""
        from functools import partial
        def multiply(x, y):
            return x * y
        double = partial(multiply, 2)
        print("Partial function result:", double(5))


if __name__ == "__main__":
    # Testing some functions
    basic = BasicFunctionConcepts()
    basic.basic_function()
    basic.function_with_args("Alice", 25)
    basic.function_with_kwargs(name="Bob", age=40)
    
    scope = ScopeOfVariables()
    scope.local_scope_example()
    scope.global_scope_example()
    
    recursion = RecursionExample()
    print("Factorial of 5:", recursion.factorial(5))
    
    advanced = AdvancedFunctionTopics()
    advanced.lambda_example()
    
    generator = GeneratorsAndComposition()
    for val in generator.simple_generator(3):
        print("Generated Value:", val)
    
    metaclass_demo = MetaclassesAndPartialFunctions()
    metaclass_demo.partial_function_example()
