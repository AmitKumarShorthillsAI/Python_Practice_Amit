class SetOperations:
    def __init__(self, initial_set):
        self.set_data = initial_set
    
    # Printing the set
    def print_set(self):
        print("Set:", self.set_data)
    
    # Adding an element to the set
    def add_element(self, element):
        self.set_data.add(element)
        print(f"Added {element} to the set")
    
    # Removing an element from the set
    def remove_element(self, element):
        if element in self.set_data:
            self.set_data.remove(element)
            print(f"Removed {element} from the set")
        else:
            print(f"Element {element} not found in the set")
    
    # Checking if an element exists in the set
    def check_element(self, element):
        print(f"Element {element} exists in set:", element in self.set_data)
    
    # Set Union
    def union_sets(self, another_set):
        result = self.set_data.union(another_set)
        print("Union of sets:", result)
    
    # Set Intersection
    def intersection_sets(self, another_set):
        result = self.set_data.intersection(another_set)
        print("Intersection of sets:", result)
    
    # Set Difference
    def difference_sets(self, another_set):
        result = self.set_data.difference(another_set)
        print("Difference of sets:", result)
    
    # Clearing the set
    def clear_set(self):
        self.set_data.clear()
        print("Set cleared")
    
# Execution
if __name__ == "__main__":
    set_demo = SetOperations({1, 2, 3, 4, 5})
    
    print("\nSet Operations:")
    set_demo.print_set()
    set_demo.add_element(6)
    set_demo.remove_element(3)
    set_demo.check_element(2)
    
    print("\nSet Operations with Another Set:")
    set_demo.union_sets({4, 5, 6, 7})
    set_demo.intersection_sets({2, 4, 6})
    set_demo.difference_sets({1, 2})
    
    print("\nClearing Set:")
    set_demo.clear_set()
