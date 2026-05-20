# mutable, accept duplicate values, ordered, indexed, dynamic size, heterogeneous data types

numbers = [5, 2, 9, 1, 5, 6] # Initial list
numbers.append(10) # Adds 10 to the end
numbers.insert(2, 15) # Inserts 15 at index 2
numbers.extend([20, 25, 30]) # Adds multiple elements at the end
numbers.remove(5) # Removes the first occurrence of 5
popped_item = numbers.pop(3) # Removes and stores the element at index 3
index = numbers.index(6) # Finds the index of 6
count_5 = numbers.count(5) # Counts occurrences of 5
numbers.sort() # Sorts the list in ascending order
numbers.reverse() # Reverses the list order
new_numbers = numbers.copy() # Creates a copy of the list
numbers.clear() # Removes all elements from the list