class ListOperations:
    def __init__(self, initial_list):
        self.list_data = initial_list
    
    # Printing the list
    def print_list(self):
        print("List:", self.list_data)
    
    # Adding an element to the list
    def add_element(self, element):
        self.list_data.append(element)
        print(f"Added {element} to the list")
    
    # Inserting an element at a specific index
    def insert_element(self, index, element):
        self.list_data.insert(index, element)
        print(f"Inserted {element} at index {index}")
    
    # Removing an element from the list
    def remove_element(self, element):
        if element in self.list_data:
            self.list_data.remove(element)
            print(f"Removed {element} from the list")
        else:
            print(f"Element {element} not found in the list")
    
    # Popping an element by index
    def pop_element(self, index=-1):
        if len(self.list_data) > 0:
            popped_element = self.list_data.pop(index)
            print(f"Popped element: {popped_element}")
        else:
            print("List is empty, nothing to pop")
    
    # Finding an element index
    def find_index(self, element):
        if element in self.list_data:
            print(f"Index of {element}: {self.list_data.index(element)}")
        else:
            print(f"Element {element} not found in the list")
    
    # Counting occurrences of an element
    def count_element(self, element):
        print(f"Count of {element}: {self.list_data.count(element)}")
    
    # Sorting the list
    def sort_list(self):
        self.list_data.sort()
        print("Sorted list:", self.list_data)
    
    # Reversing the list
    def reverse_list(self):
        self.list_data.reverse()
        print("Reversed list:", self.list_data)
    
    # Extending the list with another list
    def extend_list(self, another_list):
        self.list_data.extend(another_list)
        print("Extended list:", self.list_data)
    
    # Clearing the list
    def clear_list(self):
        self.list_data.clear()
        print("List cleared")
    
# Execution
if __name__ == "__main__":
    list_demo = ListOperations([10, 20, 30, 40, 50])
    
    print("\nList Operations:")
    list_demo.print_list()
    list_demo.add_element(60)
    list_demo.insert_element(2, 25)
    list_demo.remove_element(30)
    list_demo.pop_element()
    list_demo.find_index(40)
    list_demo.count_element(20)
    
    print("\nSorting and Reversing:")
    list_demo.sort_list()
    list_demo.reverse_list()
    
    print("\nExtending List:")
    list_demo.extend_list([70, 80, 90])
    
    print("\nClearing List:")
    list_demo.clear_list()