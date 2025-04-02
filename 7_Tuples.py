class TupleOperations:
    def __init__(self, initial_tuple):
        self.tuple_data = initial_tuple
    
    # Printing the tuple
    def print_tuple(self):
        print("Tuple:", self.tuple_data)
    
    # Accessing elements by index
    def access_element(self, index):
        if -len(self.tuple_data) <= index < len(self.tuple_data):
            print(f"Element at index {index}: {self.tuple_data[index]}")
        else:
            print("Index out of range")
    
    # Finding index of an element
    def find_index(self, element):
        if element in self.tuple_data:
            print(f"Index of {element}: {self.tuple_data.index(element)}")
        else:
            print(f"Element {element} not found in the tuple")
    
    # Counting occurrences of an element
    def count_element(self, element):
        print(f"Count of {element}: {self.tuple_data.count(element)}")
    
    # Slicing the tuple
    def slice_tuple(self, start, end):
        print(f"Sliced tuple [{start}:{end}]:", self.tuple_data[start:end])
    
    # Concatenating two tuples
    def concatenate_tuples(self, another_tuple):
        new_tuple = self.tuple_data + another_tuple
        print("Concatenated tuple:", new_tuple)
    
    # Checking if an element exists
    def check_existence(self, element):
        print(f"Element {element} exists:", element in self.tuple_data)
    
    # Finding min and max values (only for numeric tuples)
    def min_max(self):
        if all(isinstance(i, (int, float)) for i in self.tuple_data):
            print("Minimum value:", min(self.tuple_data))
            print("Maximum value:", max(self.tuple_data))
        else:
            print("Tuple contains non-numeric values, min/max not applicable")
    
    # Tuple length
    def tuple_length(self):
        print("Length of tuple:", len(self.tuple_data))
    
# Execution
if __name__ == "__main__":
    tuple_demo = TupleOperations((10, 20, 30, 40, 50))
    
    print("\nTuple Operations:")
    tuple_demo.print_tuple()
    tuple_demo.access_element(2)
    tuple_demo.find_index(30)
    tuple_demo.count_element(20)
    
    print("\nTuple Slicing:")
    tuple_demo.slice_tuple(1, 4)
    
    print("\nConcatenation:")
    tuple_demo.concatenate_tuples((60, 70, 80))
    
    print("\nExistence Check:")
    tuple_demo.check_existence(40)
    
    print("\nMin and Max:")
    tuple_demo.min_max()
    
    print("\nTuple Length:")
    tuple_demo.tuple_length()
