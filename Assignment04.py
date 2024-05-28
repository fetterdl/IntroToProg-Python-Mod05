# ------------------------------------------------------------------------------------------ #
# Title: Assignment04
# Desc: This assignment demonstrates using lists and files to work with data
# Change Log: (Who, When, What)
#   DFETTERS,5/23/2024,Created Script
# ------------------------------------------------------------------------------------------ #

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
FILE_NAME: str = "Enrollments.csv"

# Define the Data Variables
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
csv_data: str = ''  # Holds combined string data separated by a comma.
file_obj = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.

# Define and initialize lists
student_data: list = []
students: list = []

# Reads data from file Enrollments.csv
file_obj = open(FILE_NAME, "r")
for each_row in file_obj.readlines():
    student_data = each_row.split(',')
    student_data = [student_data[0].strip(), student_data[1].strip(), student_data[2].strip()]
    students.append(student_data)
file_obj.close()

# Present and Process the data
while True:

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        student_first_name = input("Enter the student's first name: ")
        student_last_name = input("Enter the student's last name: ")
        course_name = input("Please enter the name of the course: ")
        student_data = [student_first_name, student_last_name, course_name]
        students.append(student_data)
        continue

    # Present the current data
    elif menu_choice == "2":
        # Prints student data to screen
        print("\nThe current data is:\n")
        # For loop to set each row of students list to csv_data and print to screen in proper format
        for each in students:
            csv_data = f"{each[0]}, {each[1]}, {each[2]}"
            print(csv_data)
        continue

    # Save the data to a file
    elif menu_choice == "3":

        # opens file, writes data to file, closes file
        file_obj = open(FILE_NAME, "w")
        for each in students:
            csv_data = f"{each[0]}, {each[1]}, {each[2]}\n"
            file_obj.write(csv_data)
        file_obj.close()

        # Prints data saved to file
        print("\nYou have registered:\n")
        for each in students:
            csv_data = f"{each[0]}, {each[1]}, {each[2]}"
            print(csv_data)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop

    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
