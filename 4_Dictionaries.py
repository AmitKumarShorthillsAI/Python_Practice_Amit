class DictionaryOperations:
    def __init__(self, dictionary):
        self.dictionary = dictionary
    
    # Printing dictionary
    def print_dictionary(self):
        print("Dictionary:", self.dictionary)
    
    # Accessing dictionary values
    def access_value(self, key):
        print(f"Value for key '{key}':", self.dictionary.get(key, "Key not found"))
    
    # Adding key-value pairs
    def add_key_value(self, key, value):
        self.dictionary[key] = value
        print(f"Added ({key}: {value}) to dictionary")
    
    # Removing key-value pairs
    def remove_key(self, key):
        if key in self.dictionary:
            del self.dictionary[key]
            print(f"Removed key '{key}' from dictionary")
        else:
            print("Key not found")
    
    # Checking if a key exists
    def key_exists(self, key):
        print(f"Key '{key}' exists:", key in self.dictionary)
    
    # Iterating over dictionary
    def iterate_dictionary(self):
        print("Dictionary items:")
        for key, value in self.dictionary.items():
            print(f"{key}: {value}")
    
    # Dictionary length
    def dictionary_length(self):
        print("Number of items in dictionary:", len(self.dictionary))
    
    # Merging dictionaries
    def merge_dictionaries(self, another_dict):
        self.dictionary.update(another_dict)
        print("Merged dictionary:", self.dictionary)
    
    # Clearing dictionary
    def clear_dictionary(self):
        self.dictionary.clear()
        print("Dictionary cleared")
    
# Execution
if __name__ == "__main__":
    dict_demo = DictionaryOperations({"name": "Alice", "age": 25, "city": "New York"})
    
    print("\nDictionary Operations:")
    dict_demo.print_dictionary()
    dict_demo.access_value("age")
    dict_demo.add_key_value("profession", "Engineer")
    dict_demo.remove_key("city")
    dict_demo.key_exists("name")
    dict_demo.iterate_dictionary()
    dict_demo.dictionary_length()
    
    print("\nMerging Dictionaries:")
    dict_demo.merge_dictionaries({"country": "USA", "hobby": "Reading"})
    
    print("\nClearing Dictionary:")
    dict_demo.clear_dictionary()