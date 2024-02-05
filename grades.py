import csv

def load_grades(course_code):
    try:
        with open(f"{course_code}.csv", "r") as file:
            reader = csv.DictReader(file)
            grades = [row for row in reader]
    except FileNotFoundError:
        grades = []
    return grades

def save_grades(course_code, grades):
    with open(f"{course_code}.csv", "w", newline='') as file:
        fieldnames = ["student_code", "grade"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(grades)

def supply_grades(course_code):
    grades = load_grades(course_code)
    
    student_code = input("Enter student code: ")
    
    for grade in grades:
        if grade["student_code"] == student_code:
            print(f"Grade for student {student_code} is already available: {grade['grade']}")
            return
    
    student_grade = float(input("Enter student grade: "))
    
    new_grade = {"student_code": student_code, "grade": student_grade}
    grades.append(new_grade)
    save_grades(course_code, grades)
    print(f"Grade for student {student_code} added successfully.")




def display_student_grades(course_code):
    grades = load_grades(course_code)
    
    if not grades:
        print(f"No grades found for course {course_code}.")
    else:
        print(f"Grades for course {course_code}:")
        for grade in grades:
            print(f"Student Code: {grade['student_code']}, Grade: {grade['grade']}")
