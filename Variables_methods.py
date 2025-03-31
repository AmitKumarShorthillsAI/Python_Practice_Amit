# Defining the Employee class
class Employee:
    # Class variable (shared among all employees)
    company_name = "Shorthills Tech"
    total_employees = 0  # Keeps count of employees

    def __init__(self, name, emp_id, salary):
        # Instance variables (specific to each employee)
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

        # Updating the class variable (incrementing employee count)
        Employee.total_employees += 1

    # Instance method to display employee details
    def display_employee(self):
        print(f"Employee ID: {self.emp_id}, Name: {self.name}, Salary: ${self.salary}, Company: {Employee.company_name}")

    # Class method to modify class variable
    @classmethod
    def change_company_name(cls, new_name):
        cls.company_name = new_name
        print(f"Company name changed to: {cls.company_name}")

    # Static method (doesn't modify instance or class attributes)
    @staticmethod
    def company_policy():
        print("Company Policy: Work from office 3 days a week!")

# Creating instances (employees)
emp1 = Employee("Amit", 101, 60000)
emp2 = Employee("Rahul", 102, 55000)

# Accessing instance variables
emp1.display_employee()
emp2.display_employee()

# Accessing and modifying class variables via a class method
Employee.change_company_name("Shorthills AI")

# Display employees again to see the updated company name
emp1.display_employee()
emp2.display_employee()

# Accessing class variable directly
print(f"Total Employees: {Employee.total_employees}")  # Output: 2

# Calling a static method
Employee.company_policy()