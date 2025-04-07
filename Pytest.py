# Pytest Implementation for Calculator and Employee Classes

import pytest
from unittest.mock import patch

# --- Calculator Code ---

class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero!")
        return x / y

# --- Pytest for Calculator ---

@pytest.fixture
def calc():
    return Calculator()

def test_add(calc):
    assert calc.add(10, 5) == 15
    assert calc.add(-1, 1) == 0
    assert calc.add(-1, -1) == -2

def test_subtract(calc):
    assert calc.subtract(10, 5) == 5
    assert calc.subtract(-1, 1) == -2
    assert calc.subtract(-1, -1) == 0

def test_multiply(calc):
    assert calc.multiply(10, 5) == 50
    assert calc.multiply(-1, 1) == -1
    assert calc.multiply(-1, -1) == 1

def test_divide(calc):
    assert calc.divide(10, 5) == 2
    assert calc.divide(-1, 1) == -1
    assert calc.divide(-1, -1) == 1
    assert calc.divide(5, 2) == 2.5

    with pytest.raises(ValueError):
        calc.divide(10, 0)


# --- Employee Code ---

class Employee:
    """A sample Employee class"""

    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return f"{self.first}.{self.last}@email.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def monthly_schedule(self, month):
        import requests
        response = requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'


# --- Pytest for Employee ---

@pytest.fixture
def emp_1():
    return Employee('Corey', 'Schafer', 50000)

@pytest.fixture
def emp_2():
    return Employee('Sue', 'Smith', 60000)

def test_email(emp_1, emp_2):
    assert emp_1.email == 'Corey.Schafer@email.com'
    assert emp_2.email == 'Sue.Smith@email.com'

    emp_1.first = 'John'
    emp_2.first = 'Jane'

    assert emp_1.email == 'John.Schafer@email.com'
    assert emp_2.email == 'Jane.Smith@email.com'

def test_fullname(emp_1, emp_2):
    assert emp_1.fullname == 'Corey Schafer'
    assert emp_2.fullname == 'Sue Smith'

    emp_1.first = 'John'
    emp_2.first = 'Jane'

    assert emp_1.fullname == 'John Schafer'
    assert emp_2.fullname == 'Jane Smith'

def test_apply_raise(emp_1, emp_2):
    emp_1.apply_raise()
    emp_2.apply_raise()

    assert emp_1.pay == 52500
    assert emp_2.pay == 63000

def test_monthly_schedule(emp_1, emp_2):
    with patch('requests.get') as mocked_get:
        mocked_get.return_value.ok = True # for emp 1
        mocked_get.return_value.text = 'Success'

        schedule = emp_1.monthly_schedule('May')
        mocked_get.assert_called_with('http://company.com/Schafer/May')
        assert schedule == 'Success'

        mocked_get.return_value.ok = False # for emp 2

        schedule = emp_2.monthly_schedule('June')
        mocked_get.assert_called_with('http://company.com/Smith/June')
        assert schedule == 'Bad Response!'

# To run tests: use the command in terminal: `pytest filename.py`
