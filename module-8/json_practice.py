import json
#tysonblatter4-20 8.2

#  Load data from 'student.json'
with open("student.json", "r") as file:
    students_data = json.load(file)

#  Function to print the student list
def print_students(student_list):
    for student in student_list:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")

#  Notify and print original list
print("Original Student List:")
print_students(students_data)

# include my own info
new_student = {
    "F_Name": "Tyson",
    "L_Name": "Blatter",
    "Student_ID": 1248559,
    "Email": "tysondblatter@gmail.com"
}
students_data.append(new_student)

#  Notify and print updated list
print("\n Updated Student List:")
print_students(students_data)

# updated data back to 'student.json'
with open("student.json", "w") as file:
    json.dump(students_data, file)

print("\n The student.json file has been updated.")
