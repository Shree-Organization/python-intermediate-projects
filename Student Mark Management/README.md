# 📚 Student Marks Management System

A simple Python-based command-line application to manage student records.
This system allows users to add, view, search, update, and delete student data efficiently.

## 🚀 Features

- Add new student records (ID, Name, Marks).
- View all student records in a tabular format.
- Search students by ID.
- Update student marks with validation (0–100).
- Delete student records.
- Input validation for duplicate IDs and invalid marks.

## 🛠️ Technologies Used

- Python 3
- Built-in Data Structures (list, dict)

## 📖 Usage
1️⃣ Run the Program
```python student_management.py```

2️⃣ Menu Options

Once the program starts, you’ll see a menu like this:
```
Student Marks Management System
1. Add Student
2. View All Students
3. Search Student
4. Update Student Marks
5. Delete Student
6. Exit
```

1) Enter 1–6 to choose an option.

2) Example: To add a student, press 1.

## 📂 Project Structure
~~~
student-marks-management/
│── student_management.py   # Main program file
│── README.md               # Project documentation
~~~

✅ Input & Output Example

Add Student
```
Enter student ID: 101
Enter student name: Alice
Enter student marks (0-100): 85
Student added successfully.
```

View Students
```
Student Records:
ID        Name                 Marks     
----------------------------------------
101       Alice                85.0      
```

## 🔮 Possible Enhancements

- 1. Save/load student data to/from a CSV/JSON file for persistence.
- 2. Add validation for student names.
- 3. Support for multiple subjects and marks per subject.
- 4. Implement sorting and filtering options.
- 5. Build a GUI interface (Tkinter, PyQt, etc.).

## 👨‍💻 Author

Mantra Patil




