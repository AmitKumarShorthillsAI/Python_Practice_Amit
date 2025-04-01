import math

class MathFunctionsDemo:
    def __init__(self):
        """Initialize values for mathematical operations."""
        self.num1 = 16
        self.num2 = 3.7
    
    def math_functions(self):
        """Demonstrate various math functions."""
        print("Square Root:", math.sqrt(self.num1))
        print("Power:", math.pow(self.num1, 2))
        print("Ceil:", math.ceil(self.num2))
        print("Floor:", math.floor(self.num2))
        print("Absolute:", abs(-self.num2))
        print("Factorial:", math.factorial(5))
        print("Logarithm:", math.log(self.num1))
        print("Sine:", math.sin(math.radians(30)))
        print("Cosine:", math.cos(math.radians(60)))
        print("Tangent:", math.tan(math.radians(45)))
    
    def operator_precedence(self):
        """Demonstrate operator precedence and associativity."""
        print("Operator Precedence:", 2 + 3 * 4)  # Multiplication has higher precedence
        print("Associativity (Left to Right):", 10 - 3 + 2)  # Evaluates as (10-3)+2
        print("Parentheses Alter Precedence:", (2 + 3) * 4)
    
    def expressions_and_statements(self):
        """Demonstrate different types of expressions."""
        # Constant Expression
        constant_exp = 42
        print("Constant Expression:", constant_exp)
        
        # Arithmetic Expression
        arithmetic_exp = (10 + 5) * 2 - 3
        print("Arithmetic Expression:", arithmetic_exp)
        
        # Integral Expression
        integral_exp = int(4.5) + 3
        print("Integral Expression:", integral_exp)
        
        # Relational Expression
        relational_exp = 10 > 5
        print("Relational Expression:", relational_exp)
        
        # Logical Expression
        logical_exp = (10 > 5) and (5 < 3)
        print("Logical Expression:", logical_exp)

if __name__ == "__main__":
    # ________________________________________Math functions examples______________________________________
    # Create an object of the class
    math_demo = MathFunctionsDemo()
    
    # Demonstrate different math functions
    math_demo.math_functions()
    math_demo.operator_precedence()
    math_demo.expressions_and_statements()
