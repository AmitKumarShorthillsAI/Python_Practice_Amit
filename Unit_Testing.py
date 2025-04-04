import unittest
from unittest.mock import MagicMock, patch
from functools import partial, reduce

# I. Understanding Unit Testing
class UnitTestingBasics:
    def explain_basics(self):
        print("Unit Test: Testing smallest piece of code (a function/method) in isolation.")
        print("Why Unit Test? To catch bugs early and verify correctness.")
        print("Benefits: Early bug detection, refactoring safety, documentation of behavior.")


# II. unittest Framework with Practical Calculator Example
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


class TestCalculator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(5, 3), 8)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 5), 10)

    def test_divide(self):
        self.assertEqual(self.calc.divide(20, 4), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

    def test_type_check(self):
        self.assertIsInstance(self.calc.multiply(2, 3), int)

    @unittest.skip("Skipping subtraction test")
    def test_skip_example(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(self.calc.add(2, 2), 5)  # Expected to fail


# III. Test Suite Example
class TestSuiteExample:
    def create_suite(self):
        suite = unittest.TestSuite()
        suite.addTest(TestCalculator('test_add'))
        suite.addTest(TestCalculator('test_divide'))
        return suite


# IV. Mocking and Stubbing
class WeatherService:
    def get_temperature(self):
        return 35

class WeatherReporter:
    def __init__(self, service):
        self.service = service

    def report(self):
        temp = self.service.get_temperature()
        return f"The temperature is {temp}°C"

class TestWeatherReporter(unittest.TestCase):
    def test_with_mocked_temperature(self):
        mock_service = MagicMock()
        mock_service.get_temperature.return_value = 22
        reporter = WeatherReporter(mock_service)
        result = reporter.report()
        self.assertEqual(result, "The temperature is 22°C")


# V. TDD Example
class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def total_items(self):
        return len(self.items)


class TestOrder(unittest.TestCase):
    def test_order_flow(self):
        order = Order()
        self.assertEqual(order.total_items(), 0)
        order.add_item("Book")
        order.add_item("Pen")
        self.assertEqual(order.total_items(), 2)


# VI. Pytest Example - Simulated using functions

def test_pytest_style_add():
    calc = Calculator()
    assert calc.add(3, 2) == 5

def test_pytest_style_divide_by_zero():
    calc = Calculator()
    try:
        calc.divide(5, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"


# VII. Testing File I/O
class FileHandler:
    def write_file(self, filename, content):
        with open(filename, 'w') as f:
            f.write(content)

    def read_file(self, filename):
        with open(filename, 'r') as f:
            return f.read()


class TestFileHandler(unittest.TestCase):
    def setUp(self):
        self.handler = FileHandler()
        self.test_filename = "testfile.txt"

    def test_write_and_read(self):
        content = "Hello, unit testing!"
        self.handler.write_file(self.test_filename, content)
        read_content = self.handler.read_file(self.test_filename)
        self.assertEqual(content, read_content)


# VIII. Custom Assertions
class TestCustomAssertions(unittest.TestCase):
    def assertStringHasLength(self, value, length):
        self.assertEqual(len(value), length)

    def test_string_length_check(self):
        self.assertStringHasLength("Python", 6)


# Entry Point to Run All Tests
if __name__ == '__main__':
    print("\n--- Unit Testing Overview ---")
    basics = UnitTestingBasics()
    basics.explain_basics()

    print("\n--- Running Test Suite ---")
    suite = TestSuiteExample().create_suite()
    runner = unittest.TextTestRunner()
    runner.run(suite)

    print("\n--- Running Full Unit Tests ---")
    unittest.main(exit=False)
