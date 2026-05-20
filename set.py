# mutable, unordered, unindexed, dynamic size, heterogeneous data types, no duplicate values

# Each value in a set is hashed using a hash function hash() in Python.
# The hash is used as an index to store the element in memory.

# not that much used in real life applications

a = {1, 2, 3, 4, 5} # Initial set
b = {4, 5, 6, 7, 8} # Another set
a.add(9) # Adds 9 to the set
a.update({10, 11, 12}) # Adds multiple elements to the set
a.remove(2) # Removes 2 from the set
a.discard(3) # Removes 3 from the set, does nothing if 3 is not present
popped_element = a.pop() # Removes and returns an arbitrary element from the set
intersection = a.intersection(b) # Returns a new set with common elements
union = a.union(b) # Returns a new set with all unique elements from both sets  
difference = a.difference(b) # Returns a new set with elements in a but not in b
symmetric_difference = a.symmetric_difference(b) # Returns a new set with elements in either a or b but not in both
is_subset = a.issubset(b) # Checks if a is a subset of b
is_superset = a.issuperset(b) # Checks if a is a superset of b
is_disjoint = a.isdisjoint(b) # Checks if a and b have no elements in common

# Set operations using operators
print(a | b) # Union
print(a & b) # Intersection
print(a - b) # Difference
print(a^b) # Symmetric Difference
