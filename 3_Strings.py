class StringOperations:
    def __init__(self, text):
        self.text = text

    def print_string(self):
        """Print the original string."""
        print("Original String:", self.text)

    def string_indexing(self):
        """Demonstrate string indexing."""
        print("First Character:", self.text[0])
        print("Last Character:", self.text[-1])

    def string_slicing(self):
        """Demonstrate string slicing."""
        print("First 5 characters:", self.text[:5])
        print("Characters from index 3 to 8:", self.text[3:9])
        print("Last 5 characters:", self.text[-5:])

    def string_methods(self):
        """Demonstrate various string methods."""
        print("Uppercase:", self.text.upper())
        print("Lowercase:", self.text.lower())
        print("Title Case:", self.text.title())
        print("Swap Case:", self.text.swapcase())
        print("Replace 'e' with '*':", self.text.replace('e', '*'))

    def string_split_join(self):
        """Demonstrate split and join operations."""
        words = self.text.split(" ")
        print("Split into words:", words)
        print("Join with hyphen:", "-".join(words))

    def string_search_count(self):
        """Search for a substring and count occurrences."""
        print("Position of 'is':", self.text.find("is"))
        print("Occurrences of 's':", self.text.count("s"))

    def string_checks(self):
        """Check string properties."""
        print("Is alphabetic:", self.text.isalpha())
        print("Is alphanumeric:", self.text.isalnum())
        print("Starts with 'This':", self.text.startswith("This"))
        print("Ends with 'text':", self.text.endswith("text"))

    def string_formatting(self, name, age):
        """Demonstrate different string formatting methods."""
        print(f"My name is {name} and I am {age} years old.")
        print("My name is {} and I am {} years old.".format(name, age))
        print("My name is %s and I am %d years old." % (name, age))

# Execution
if __name__ == "__main__":
    str_demo = StringOperations("This is a sample text for testing string operations.")
    
    print("\nString Operations:")
    str_demo.print_string()
    str_demo.string_indexing()
    str_demo.string_slicing()
    
    print("\nString Methods:")
    str_demo.string_methods()
    
    print("\nString Split & Join:")
    str_demo.string_split_join()
    
    print("\nString Search & Count:")
    str_demo.string_search_count()
    
    print("\nString Checks:")
    str_demo.string_checks()
    
    print("\nString Formatting:")
    str_demo.string_formatting("John", 30)
