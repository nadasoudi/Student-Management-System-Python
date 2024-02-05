
import json
import csv
import os

def load_students():
    students = []
    if os.path.exists("students.json"):
        with open("students.json", "r") as file:
            students = json.load(file)
    return students

def load_courses():
    courses = []
    if os.path.exists("courses.json"):
        with open("courses.json", "r") as file:
            courses = json.load(file)
    return courses

def load_grades(course_code):
    grades = []
    file_path = f"{course_code}.csv"
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)
            grades = [row for row in reader]
    return grades

def calculate_gpa(student_code):
    total_credit_hours = 0
    total_quality_points = 0

    courses = load_courses()

    for course in courses:
        course_code = course["code"]
        course_grades = load_grades(course_code)

        student_grade_record = next((g for g in course_grades if g["student_code"] == student_code), None)

        if student_grade_record is not None:
            credit_hours = course.get("credit_hours", 0)
            total_credit_hours += credit_hours

            numeric_grade = float(student_grade_record["grade"])
            letter_grade = calculate_letter_grade(numeric_grade)

            quality_points = calculate_quality_points(letter_grade)
            total_quality_points += credit_hours * quality_points

    if total_credit_hours == 0:
        return 0

    gpa = total_quality_points / total_credit_hours
    return round(gpa, 2)

def calculate_letter_grade(numeric_grade):
    if numeric_grade >= 90:
        return 'A'
    elif numeric_grade >= 80:
        return 'B'
    elif numeric_grade >= 70:
        return 'C'
    elif numeric_grade >= 60:
        return 'D'
    else:
        return 'F'

def calculate_quality_points(letter_grade):
    if letter_grade == 'A':
        return 4.0
    elif letter_grade == 'B':
        return 3.0
    elif letter_grade == 'C':
        return 2.0
    elif letter_grade == 'D':
        return 1.0
    else:
        return 0.0

def generate_student_result(student_code):
    students = load_students()
    student = next((s for s in students if s["code"] == student_code), None)

    if student is not None:
        gpa = calculate_gpa(student_code)

        with open(f"{student_code}.html", "w") as html_file:
            html_file.write("<html><head><title>Student Result</title></head><body>")
            html_file.write(f"<h1>Student Result for {student['name']} (Code: {student['code']})</h1>")
            html_file.write(f"<h2>GPA: {gpa}</h2>")

            courses = load_courses()
            for course in courses:
                course_code = course["code"]
                course_grades = load_grades(course_code)

                student_grade_record = next((g for g in course_grades if g["student_code"] == student_code), None)

                if student_grade_record is not None:
                    numeric_grade = float(student_grade_record["grade"])
                    letter_grade = calculate_letter_grade(numeric_grade)
                    html_file.write(f"<p>{course['name']} - Grade: {numeric_grade} ({letter_grade})</p>")

            html_file.write("</body></html>")

        print(f"Result for student {student['name']} (Code: {student['code']}) generated successfully with GPA: {gpa}.")
    else:
        print(f"Student with code {student_code} not found.")
