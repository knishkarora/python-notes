# File handling means Creating, Reading, Updating, Deleting(CRUD) operations that we can perform in files.
# To work with files in Python, we use the built-in open() function, which returns a file object.
# The open() function takes two arguments: the file name and the mode in which to open the file.
# The mode can be:
# 'r' - Read mode (default): Opens the file for reading. If the file does not exist, it raises a FileNotFoundError.
# 'w' - Write mode: Opens the file for writing. If the file already exists, it truncates the file to zero length. If the file does not exist, it creates a new file.
# 'a' - Append mode: Opens the file for writing. If the file already exists, it appends the new data to the end of the file. If the file does not exist, it creates a new file.
# 'x' - Exclusive creation mode: Opens the file for exclusive creation. If the file already exists, it raises a FileExistsError. If the file does not exist, it creates a new file.
# 'b' - Binary mode: Opens the file in binary mode. This is used for non-text files like images or videos.
# 't' - Text mode (default): Opens the file in text mode. This is used for text files.
# 'r+' - Read and write mode: Opens the file for both reading and writing. If the file does not exist, it raises a FileNotFoundError.
# 'w+' - Write and read mode: Opens the file for both writing and reading. If the file already exists, it truncates the file to zero length. If the file does not exist, it creates a new file.

# Example of creating and writing to a file:
# file = open("myfile.txt", "r")
# print(file.read()) #full
# print(file.readline()) # 1 file
# print(file.readlines()) # full into a list
# file.close()

# use with keyword no need to close the file
# Example of using with statement to handle files:
# with open("myfile.txt", "r") as file:
#     content = file.read()
#     print(content) 


# practice question:
with open("student.txt", "a+") as file:
    # 1. Move pointer to start so we can read existing data
    file.seek(0)
    data = file.read()
    
    clean_data = data.strip()
    lines = clean_data.split("\n")
    
    # Create a list to store all valid integer grades for the average calculation
    valid_grades = []
    
    # 2. Write a separation line in the file so you can see where your append starts
    file.write("\n--- Processing Results ---\n")
    
    for line in lines:
        # Skip empty lines to prevent crashes
        if not line.strip():
            continue
            
        # Fix: Remove the brackets around line.split()
        parts = line.split(",")
        
        name = parts[0]
        grade_str = parts[1]
        
        # 3. Error Handling: Try to convert the grade to an integer
        try:
            grade_num = int(grade_str)
            valid_grades.append(grade_num)  # Save the number for average calculation
            
            # Write individual student result directly inside the file loop
            file.write(f"{name} has a grade of {grade_num}\n")
            
        except ValueError:
            # This catches "Charlie,invalid_grade" safely without crashing
            print(f"Skipping error: Could not convert grade for {name}")
            
    # 4. Calculate the average using our valid grades list (inside the with block)
    if valid_grades:
        total_sum = sum(valid_grades)
        avg = total_sum / len(valid_grades)
        file.write(f"Average grade is {avg}\n")
    else:
        file.write("No valid grades found to compute average.\n")

print("File processing complete! Check your student.txt file.")

