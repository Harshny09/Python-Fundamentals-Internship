import json
import os

FILE_NAME = "students.json"

# Load student data
def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save student data
def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

# Add student
def add_student(students):
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    department = input("Enter department: ")

    student = {
        "Name": name,
        "Roll No": roll_no,
        "Department": department
    }

    students.append(student)
    save_students(students)
    print("Student added successfully!")

# View students
def view_students(students):
    if not students:
        print("No student records found.")
        return

    print("\nStudent Records:")
    for student in students:
        print("--------------------")
        for key, value in student.items():
            print(f"{key}: {value}")

# Search student
def search_student(students):
    roll_no = input("Enter roll number to search: ")

    for student in students:
        if student["Roll No"] == roll_no:
            print("\nStudent Found:")
            for key, value in student.items():
                print(f"{key}: {value}")
            return

    print("Student not found.")

# Delete student
def delete_student(students):
    roll_no = input("Enter roll number to delete: ")

    for student in students:
        if student["Roll No"] == roll_no:
            students.remove(student)
            save_students(students)
            print("Student deleted successfully!")
            return

    print("Student not found.")

# Main menu
def main():
    students = load_students()

    while True:
        print("\n===== Student Record Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()