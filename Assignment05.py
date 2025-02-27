# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   <Your Name Here>,<Date>, <Activity>
# ------------------------------------------------------------------------------------------ #

import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.

# When the program starts, read the file data into a 2d list table (a list of dictionary rows)
# Extract the data from the file
try:
    file = open(FILE_NAME, "r")
    json_file = json.load(file)
    for student in json_file:
        student_data = {
            'FirstName': student['FirstName'],
            'LastName': student['LastName'],
            'CourseName': student['CourseName']
        }
        students.append(student_data)
    file.close()
# the file doesnt exist
except FileNotFoundError as e:
    print("Error: File not found, validate location or name is as expected.")
    print(e.__doc__, type(e), sep='\n')
    print("")
except Exception as e:
    print("Error: There was a non-specific error.")
    print(e, e.__doc__, type(e), sep='\n')
    print("")

# Present and Process the data
while True:

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")
    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should only include letters")
            student_last_name = input("Enter the student's last name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should only include letters")
            course_name = input("Please enter the name of the course: ")
            new_student = {
                'FirstName': student_first_name,
                'LastName': student_last_name,
                'CourseName': course_name
            }
            students.append(new_student)
            print(f"You have registered {new_student['FirstName']} {new_student['LastName']} for {new_student['CourseName']}.")
        # the input passed to first or last name are the incorrect type
        except ValueError as e:
            print(e)  # Prints message
            print('Built-In Python error info: ')
            print(e, e.__doc__, type(e), sep='\n')
        continue

    # Present the current data
    elif menu_choice == "2":
        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f"Student {student['FirstName']} {student['LastName']} is enrolled in {student['CourseName']}")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file, indent=4)
            file.close()
            print("The following data was saved to file!")
            for student in students:
                print(f"Student {student['FirstName']} {student['LastName']} is enrolled in {student['CourseName']}")
        except TypeError as e:
            print("Invalid format\n")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print('There was an unspecified error!\n')
            print(e, e.__doc__, type(e), sep='\n')

        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
