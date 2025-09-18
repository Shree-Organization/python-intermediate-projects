# Student Marks Management System

# Data structure to hold student records
# Each student record is a dictionary with keys: 'id', 'name', 'marks'
students = []

def add_student():
    student_id = input("Enter student ID: ")
    # Check if student ID already exists
    for student in students:
        if student['id'] == student_id:
            print("Student ID already exists!")
            return
    name = input("Enter student name: ")
    try:
        marks = float(input("Enter student marks (0-100): "))
        if marks < 0 or marks > 100:
            print("Marks should be between 0 and 100.")
            return
    except ValueError:
        print("Invalid marks input.")
        return
    students.append({'id': student_id, 'name': name, 'marks': marks})
    print("Student added successfully.")

def view_students():
    if not students:
        print("No student records found.")
        return
    print("\nStudent Records:")
    print(f"{'ID':<10}{'Name':<20}{'Marks':<10}")
    print("-" * 40)
    for student in students:
        print(f"{student['id']:<10}{student['name']:<20}{student['marks']:<10}")
    print()

def search_student():
    student_id = input("Enter student ID to search: ")
    for student in students:
        if student['id'] == student_id:
            print(f"Student found: ID={student['id']}, Name={student['name']}, Marks={student['marks']}")
            return
    print("Student not found.")

def update_student():
    student_id = input("Enter student ID to update: ")
    for student in students:
        if student['id'] == student_id:
            try:
                new_marks = float(input(f"Enter new marks for {student['name']} (0-100): "))
                if new_marks < 0 or new_marks > 100:
                    print("Marks should be between 0 and 100.")
                    return
                student['marks'] = new_marks
                print("Marks updated successfully.")
                return
            except ValueError:
                print("Invalid marks input.")
                return
    print("Student not found.")

def delete_student():
    student_id = input("Enter student ID to delete: ")
    for i, student in enumerate(students):
        if student['id'] == student_id:
            del students[i]
            print("Student record deleted.")
            return
    print("Student not found.")

def main():
    while True:
        print("\nStudent Marks Management System")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student Marks")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()


# Possible Enhancements
# Save/load student data to/from a file (e.g., CSV or JSON) to persist data between runs.
# Add validation for student names.
# Add more fields like subjects and marks per subject.
# Implement sorting and filtering options.
# Create a GUI using Tkinter or other frameworks.