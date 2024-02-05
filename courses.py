
import json

def load_courses():
    try:
        with open("courses.json", "r") as file:
            courses = json.load(file)
    except FileNotFoundError:
        courses = []
    return courses

def save_courses(courses):
    with open("courses.json", "w") as file:
        json.dump(courses, file, indent=2)

def add_course(code, name, max_degree, credit_hours):  
    courses = load_courses()
    new_course = {"code": code, "name": name, "max_degree": max_degree, "credit_hours": credit_hours} 
    courses.append(new_course)
    save_courses(courses)
    print(f"Course {name} added successfully.")

def edit_course(code, new_name, new_max_degree, new_credit_hours):  
    courses = load_courses()
    for course in courses:
        if course["code"] == code:
            course["name"] = new_name
            course["max_degree"] = new_max_degree
            course["credit_hours"] = new_credit_hours  
            save_courses(courses)
            print(f"Information for course with code {code} updated successfully.")
            return
    print(f"Course with code {code} not found.")

def remove_course(code):
    courses = load_courses()
    for course in courses:
        if course["code"] == code:
            courses.remove(course)
            save_courses(courses)
            print(f"Course with code {code} removed successfully.")
            return
    print(f"Course with code {code} not found.")

def display_courses():
    courses = load_courses()
    if not courses:
        print("No courses found.")
    else:
        print("Courses Information:")
        for course in courses:
            print(f"Code: {course['code']}, Name: {course['name']}, Max Degree: {course['max_degree']}, Credit Hours: {course.get('credit_hours', 0)}")
