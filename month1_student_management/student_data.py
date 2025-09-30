# month1_student_management/student_data.py

students = []

def add_student():
    """
    Prompt the user to enter student name, age, and grade.
    Append the student as a dictionary to the students list.
    """
    name = input("Enter student name: ").strip()
    
    # Validate age input
    while True:
        age = input("Enter student age: ").strip()
        if age.isdigit() and int(age) > 0:
            age = int(age)
            break
        else:
            print("Invalid age. Please enter a positive number.")
    
    # Validate grade input
    while True:
        grade = input("Enter student grade (0-100): ").strip()
        try:
            grade = float(grade)
            if 0 <= grade <= 100:
                break
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid grade. Please enter a number between 0 and 100.")
    
    student = {
        "name": name,
        "age": age,
        "grade": grade
    }
    
    students.append(student)
    print(f"Student {name} added successfully!")

def view_students():
    """
    Loop through the students list and print each student's info.
    """
    if not students:
        print("No students found.")
        return
    
    print("\nList of Students:")
    for idx, student in enumerate(students, start=1):
        print(f"{idx}. Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

def get_average_grade():
    """
    Return the average grade of all students.
    """
    if not students:
        return 0.0
    
    total = sum(student["grade"] for student in students)
    average = total / len(students)
    return average
