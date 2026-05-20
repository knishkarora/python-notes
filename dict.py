# key-value pairs, mutable, unordered, indexed, dynamic size, heterogeneous data types, no duplicate keys
# we can perform CRUD(create, read, update, delete) operations on values

my_dict = {"name": "Alice", "age": 30, "city": "New York"} # Initial dictionary
my_dict["email"] = "alice@example.com" # Adding a new key-value pair
print(my_dict["name"]) # Reading a value by key
my_dict["age"] = 31 # Updating a value
del my_dict["city"] # Deleting a key-value pair
keys = my_dict.keys() # Returns a view of keys
values = my_dict.values() # Returns a view of values
items = my_dict.items() # Returns a view of key-value pairs
my_dict.clear() # Removes all key-value pairs from the dictionary
my_dict_copy = my_dict.copy() # Creates a shallow copy of the dictionary


print(my_dict) # Output: {}
print(my_dict_copy) # Output: {'name': 'Alice', 'age': 31, 'email': 'alice@example.com'}
