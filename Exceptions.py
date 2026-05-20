# try ==> Wrap the block of code that might cause an exception.
# except ==> Handle the exception if it occurs.
# else ==> Execute this block if no exception occurs.
# finally ==> Execute this block regardless of whether an exception occurred or not.
# raise ==> Manually raise an exception.

# different types of exceptions:
# 1. ValueError: Raised when a function receives an argument of the right type but an inappropriate value.
# 2. TypeError: Raised when an operation or function is applied to an object of inappropriate type.
# 3. IndexError: Raised when a sequence subscript is out of range.  
# 4. KeyError: Raised when a dictionary key is not found.
# 5. FileNotFoundError: Raised when a file or directory is requested but doesn't exist.
# 6. ZeroDivisionError: Raised when the second argument of a division or modulo operation is zero.
# 7. ImportError: Raised when an import statement fails to find the module definition or when a from ... import fails to find a name that is to be imported.
# 8. AttributeError: Raised when an attribute reference or assignment fails.
# 9. NameError: Raised when a local or global name is not found.

# Example of using try, except, else, finally, and raise:
def divide(a, b):
    try:
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        result = a / b
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print(f"The result of {a} divided by {b} is: {result}")
    finally:
        print("Execution of the divide function is complete.")

# Example usage:
divide(10, 2)  # This will execute the else block and print the result  
divide(10, 0)  # This will raise a ValueError and execute the except block

# other example of handling multiple exceptions:
def process_data(data):
    try:
        # Simulating a potential error in data processing
        if not isinstance(data, list):
            raise TypeError("Data must be a list.")
        if len(data) == 0:
            raise ValueError("Data list cannot be empty.")
        # Process the data (for example, summing the numbers)
        result = sum(data)
    except TypeError as e:
        print(f"Type Error: {e}")
    except ValueError as e:
        print(f"Value Error: {e}")
    else:
        print(f"The sum of the data is: {result}")
    finally:
        print("Execution of the process_data function is complete.")

# Example usage:
process_data([1, 2, 3])  # This will execute the else block and print the result
process_data("not a list")  # This will raise a TypeError and execute the first except block
process_data([])  # This will raise a ValueError and execute the second except block
