# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   DFetters,5/26/2024,Created Script
# ------------------------------------------------------------------------------------------ #
import io
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
FILE_NAME_CSV: str = "Enrollments_csv.csv"

# Define file variables
file = io.TextIOWrapper
file_csv = None

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
json_data: str = ''
student_data: dict = {}  # one row of student data in a dictionary
students: list = []  # a table of student data
csv_data: str = ''  # Holds combined string data separated by a comma.
 # Holds a reference to an opened file.
menu_choice: str = "" # Hold the choice made by the user.

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()
except FileNotFoundError as e:
    print("\nEnrollments.json file must exist before running this script.\n")
    print("File not found.")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("There was a non-specific error.\n")
    print("-- Technical Error Message --")
    print(e, e.__doc__, type(e), sep='\n')
finally:
    if not file.closed:
        file.close()

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
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name, "LastName": student_last_name, "CourseName": course_name}
            students.append(student_data)
            print(f"You have registered {student_data["FirstName"]} {student_data["LastName"]} "
              f"for {student_data["CourseName"]}.")
        except ValueError as e:
            print(e)
            print("-- Technical Error Message --")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("There was a non-specific error.\n")
            print("-- Technical Error Message --")
            print(e, e.__doc__, type(e), sep='\n')
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for row in students:
            print(f"{row["FirstName"]} {row["LastName"]} is enrolled in {row["CourseName"]}")
        print("-"*50)
        continue

    # Save the data to a file

    elif menu_choice == "3":
        try:
            # Writes data to .json file
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            file.close()
            # prints data to the screen
            print("The following data was saved to file!")
            for student in students:
                print(f"{student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}")

                # creates text string for .csv file
                csv_data += f"{student["FirstName"]}, {student["LastName"]}, {student["CourseName"]}\n"

        except Exception as e:
            print("There was a non-specific error.\n")
            print("-- Technical Error Message --")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if not file.closed:
                file.close()

        # Assignment sheet indicated program must save date to a comma separated string file.
        try:
            file_csv = open(FILE_NAME_CSV, "w")
            file_csv.write(csv_data)
            file_csv.close()

        except Exception as e:
            print("There was a non-specific error.\n")
            print("-- Technical Error Message --")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if not file_csv.closed:
                file_csv.close()
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3 or 4")

print("Program Ended")
