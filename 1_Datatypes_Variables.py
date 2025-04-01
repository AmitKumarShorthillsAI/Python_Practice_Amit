class VariableExamples:
    # Class variable (shared among all instances)
    class_variable = "I am a class variable"

    def __init__(self):
        # Instance variables (unique for each object)
        self.instance_variable = "I am an instance variable"
        self.dynamic_variable = None  # Will be changed dynamically
    
    def create_variables(self):
        """Creating and modifying instance variables dynamically."""
        self.dynamic_variable = 10  # Dynamic assignment
        self.name = "John"  # String variable
        self.age = 25  # Integer variable
        self.salary = 50000.50  # Float variable
        self.is_active = True  # Boolean variable
        print("Variables Created:", self.__dict__)  # Display all instance variables
    
    def show_data_types(self):
        """Show data types of variables."""
        print("Data Types:")
        print("Name Type:", type(self.name))
        print("Age Type:", type(self.age))
        print("Salary Type:", type(self.salary))
        print("Active Type:", type(self.is_active))

    @staticmethod
    def variable_naming():
        """Demonstrate different variable naming conventions."""
        camelCase = "Camel Case"
        PascalCase = "Pascal Case"
        snake_case = "Snake Case"
        print("Variable Naming Styles:")
        print("camelCase:", camelCase)
        print("PascalCase:", PascalCase)
        print("snake_case:", snake_case)

    def multiple_assignments(self):
        """Demonstrate multiple assignments."""
        x, y, z = "Apple", "Banana", "Cherry"  # Multiple assignments
        print("Multiple Assignments:", x, y, z)

        a = b = c = "Same Value"  # One value to multiple variables
        print("One Value to Multiple Variables:", a, b, c)

    def unpacking_collections(self):
        """Demonstrate unpacking collections."""
        fruits = ["Mango", "Orange", "Grapes"]
        x, y, z = fruits  # Unpacking
        print("Unpacked Variables:", x, y, z)

    def output_variables(self):
        """Demonstrate different ways to output variables."""
        lang = "Python"
        print("Simple Print:", lang)
        print("Multiple Variables:", lang, "is", "awesome")
        print("String Concatenation:", lang + " is great")

    def math_operations(self):
        """Demonstrate variables in mathematical operations."""
        num1, num2 = 10, 20
        print("Sum:", num1 + num2)  # Addition
        print("Multiplication:", num1 * num2)  # Multiplication

    def global_variable_demo(self):
        """Demonstrate global and local variable usage."""
        global global_var
        global_var = "I am a global variable, before modification"
        print("Global Variable Inside Method:", global_var)
    
    def modify_global_variable(self):
        """Modify global variable inside a method."""
        global global_var
        global_var = "Global variable modified"
        print("Modified Global Variable:", global_var)
    
    def local_variable_demo(self):
        """Demonstrate local variables."""
        local_var = "I am a local variable"
        print("Local Variable:", local_var)

# Creating object of the class
var_obj = VariableExamples()

# Demonstrate different variable methods
var_obj.create_variables()
var_obj.show_data_types()
var_obj.variable_naming()
var_obj.multiple_assignments()
var_obj.unpacking_collections()
var_obj.output_variables()
var_obj.math_operations()

# Global variable demonstrations
var_obj.global_variable_demo()
var_obj.modify_global_variable()
print("Access Global Variable Outside Class:", global_var)

# Local variable demonstration
var_obj.local_variable_demo()

# Accessing class and instance variables
print("Class Variable:", VariableExamples.class_variable)
print("Instance Variable:", var_obj.instance_variable)


# ________________________________________Data type examples______________________________________
class DataTypesDemo:
    def __init__(self):
        """Initialize integer, float, string, and boolean variables."""
        self.decimal_int = 10000  # Decimal integer
        self.large_int = 9876543210123456789  # Large integer
        self.binary_int = 0b1010  # Binary (10 in decimal)
        self.octal_int = 0o12  # Octal (10 in decimal)
        self.hexadecimal_int = 0xA  # Hexadecimal (10 in decimal)
        
        self.float_num = 123.456  # Float number
        self.scientific_notation = 1.23e3  # Scientific notation (1230.0)
        
        self.string_data = "Hello, Python!"  # String type
        self.boolean_true = True  # Boolean type
        self.boolean_false = False  # Boolean type
    
    def display_int_types(self):
        """Display integer types and their conversions."""
        print("Decimal Integer:", self.decimal_int)
        print("Large Integer:", self.large_int)
        print("Binary Integer (0b1010):", self.binary_int)
        print("Octal Integer (0o12):", self.octal_int)
        print("Hexadecimal Integer (0xA):", self.hexadecimal_int)
    
    def convert_to_decimal(self):
        """Convert binary, octal, and hexadecimal to decimal."""
        print("Binary to Decimal:", int("1010", 2))
        print("Octal to Decimal:", int("12", 8))
        print("Hexadecimal to Decimal:", int("A", 16))
    
    def display_float_types(self):
        """Display float values and scientific notation."""
        print("Float Number:", self.float_num)
        print("Scientific Notation:", self.scientific_notation)
    
    def display_string_data(self):
        """Display string data and its operations."""
        print("String:", self.string_data)
        print("Upper Case:", self.string_data.upper())
        print("Lower Case:", self.string_data.lower())
        print("String Length:", len(self.string_data))
    
    def display_boolean_values(self):
        """Display boolean values and their numeric representation."""
        print("Boolean True:", self.boolean_true)
        print("Boolean False:", self.boolean_false)
        print("Boolean as Integer:", int(self.boolean_true), int(self.boolean_false))

# Create object of the class
data_obj = DataTypesDemo()

data_obj.display_int_types()
data_obj.convert_to_decimal()
data_obj.display_float_types()
data_obj.display_string_data()
data_obj.display_boolean_values()
