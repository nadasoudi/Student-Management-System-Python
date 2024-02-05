import json

def load_students():
    try:
        with open("students.json", "r") as file:
            students = json.load(file)
    except FileNotFoundError:
        students = []
    return students

def save_students(students):
    with open("students.json", "w") as file:
        json.dump(students, file, indent=2)

def add_student(code, name, birthdate):
    students = load_students()
    new_student = {"code": code, "name": name, "birthdate": birthdate}
    students.append(new_student)
    save_students(students)
    print(f"Student {name} added successfully.")

def edit_student(code, new_name, new_birthdate):
    students = load_students()
    for student in students:
        if student["code"] == code:
            student["name"] = new_name
            student["birthdate"] = new_birthdate
            save_students(students)
            print(f"Information for student with code {code} updated successfully.")
            return
    print(f"Student with code {code} not found.")

def remove_student(code):
    students = load_students()
    for student in students:
        if student["code"] == code:
            students.remove(student)
            save_students(students)
            print(f"Student with code {code} removed successfully.")
            return
    print(f"Student with code {code} not found.")

def display_students():
    students = load_students()
    if not students:
        print("No students found.")
    else:
        print("Students Information:")
        for student in students:
            print(f"Code: {student['code']}, Name: {student['name']}, Birthdate: {student['birthdate']}")

