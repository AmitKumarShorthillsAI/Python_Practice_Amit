import os

class FileManager:
    """Class for handling file operations."""
    
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def open_file(self):
        """Opens the file in the given mode."""
        try:
            self.file = open(self.filename, self.mode)
            print(f"File '{self.filename}' opened in '{self.mode}' mode.")
        except FileNotFoundError:
            print("Error: File not found!")
        except PermissionError:
            print("Error: Permission denied!")
    
    def read_file(self):
        """Reads the entire content of the file."""
        if self.file:
            return self.file.read()
        print("Error: File not opened!")
    
    def read_lines(self):
        """Reads file line by line."""
        if self.file:
            return self.file.readlines()
        print("Error: File not opened!")
    
    def write_file(self, content):
        """Writes content to the file."""
        if self.file:
            self.file.write(content)
            print("Content written successfully.")
        else:
            print("Error: File not opened in write mode!")
    
    def append_file(self, content):
        """Appends content to the file."""
        if self.file:
            self.file.write(content)
            print("Content appended successfully.")
        else:
            print("Error: File not opened in append mode!")
    
    def close_file(self):
        """Closes the file to release resources."""
        if self.file:
            self.file.close()
            print("File closed successfully.")
        else:
            print("Error: File not opened!")

class DirectoryManager:
    """Class for handling directory operations."""
    
    @staticmethod
    def create_directory(directory):
        """Creates a new directory if it doesn't exist."""
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Directory '{directory}' created.")
        else:
            print("Directory already exists!")
    
    @staticmethod
    def delete_directory(directory):
        """Deletes a directory if it exists."""
        if os.path.exists(directory):
            os.rmdir(directory)
            print(f"Directory '{directory}' deleted.")
        else:
            print("Directory not found!")
    
    @staticmethod
    def list_directory(path="."):
        """Lists files and directories in the given path."""
        return os.listdir(path)

class ExceptionHandler:
    """Class to demonstrate exception handling in Python."""
    
    @staticmethod
    def handle_division(a, b):
        """Handles ZeroDivisionError exception."""
        try:
            return a / b
        except ZeroDivisionError:
            print("Error: Cannot divide by zero!")
    
    @staticmethod
    def handle_multiple_exceptions():
        """Handles multiple exceptions."""
        try:
            num = int("Hello")
        except (ValueError, TypeError) as e:
            print(f"Error: {e}")
    
    @staticmethod
    def custom_exception():
        """Raises a custom exception."""
        class CustomError(Exception):
            pass
        try:
            raise CustomError("This is a custom error!")
        except CustomError as e:
            print(f"Custom Exception Caught: {e}")

    @staticmethod
    def use_assertion(value):
        """Uses assert statement for debugging."""
        try:
            assert value > 0, "Value must be greater than zero!"
        except AssertionError as e:
            print(f"Assertion Error: {e}")

if __name__ == "__main__":
    # File handling
    file_manager = FileManager("test.txt", "w")
    file_manager.open_file()
    file_manager.write_file("Hello, World!\n")
    file_manager.close_file()
    
    # Directory handling
    DirectoryManager.create_directory("test_dir")
    DirectoryManager.list_directory()
    DirectoryManager.delete_directory("test_dir")
    
    # Exception Handling
    ExceptionHandler.handle_division(10, 0)
    ExceptionHandler.handle_multiple_exceptions()
    ExceptionHandler.custom_exception()
    ExceptionHandler.use_assertion(-5)
