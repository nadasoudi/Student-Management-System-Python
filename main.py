import argparse, os
import matplotlib.pyplot as plt
from results import load_students, load_courses, load_grades, calculate_gpa

def run_demo(out_dir: str):
    os.makedirs(out_dir, exist_ok=True)
    students = load_students()
    courses  = load_courses()
    grades   = load_grades()

    html_path = os.path.join(out_dir, "index.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write("<!doctype html><meta charset='utf-8'><title>Student Summary</title>")
        f.write("<h1>Student Management System — Demo</h1>")
        f.write(f"<p>Students: {len(students)} | Courses: {len(courses)}</p>")
        f.write("<table border='1' cellpadding='6'><tr><th>Code</th><th>Name</th><th>GPA</th></tr>")
        for s in sorted(students, key=lambda x: x.get('code','')):
            gpa = calculate_gpa(s.get('code'), grades, courses)
            f.write(f"<tr><td>{s.get('code')}</td><td>{s.get('name')}</td><td>{gpa:.2f}</td></tr>")
        f.write("</table>")

    labels, counts = [], []
    for c in sorted(courses, key=lambda x: x.get('code','')):
        code = c.get('code'); labels.append(code)
        counts.append(len(grades.get(code, {})))
    plt.figure()
    plt.bar(labels, counts)
    plt.title("Registrations per Course")
    plt.xlabel("Course"); plt.ylabel("# Students with grade")
    chart_path = os.path.join(out_dir, "registrations_per_course.png")
    plt.tight_layout(); plt.savefig(chart_path); plt.close()
    print(f"[demo] wrote: {html_path}")
    print(f"[demo] wrote: {chart_path}")

from students import *
from courses import *
from grades import *
from results import *
from statics import *
while True:
    print("Students Program:")
    print("----")
    print("(1) Add/Edit/Remove students information")
    print("(2) Courses information")
    print("(3) Supply / view  grades to students per course ")
    print("(4) Final result")
    print("(5) Pie")
    print("(6) Exit")
    
    user_choice = int(input("Pick a number (1-6): "))
    

    if user_choice == 1:
        print("(a) Add student")
        print("(b) Edit student")
        print("(c) Remove student")
        print("(d) Display students information")

        student_operation = input("Choose an operation (a-d): ")

        if student_operation == 'a':
            code = input("Enter student code: ")
            name = input("Enter student name: ")
            birthdate = input("Enter student birthdate: ")
            add_student(code, name, birthdate)

        elif student_operation == 'b':
            code = input("Enter student code to edit: ")
            new_name = input("Enter new student name: ")
            new_birthdate = input("Enter new student birthdate: ")
            edit_student(code, new_name, new_birthdate)

        elif student_operation == 'c':
            code = input("Enter student code to remove: ")
            remove_student(code)

        elif student_operation == 'd':
            display_students()

        else:
            print("Invalid operation choice.")

    elif user_choice == 2:
        print("(a) Add course")
        print("(b) Edit course")
        print("(c) Remove course")
        print("(d) Display courses information")

        course_operation = input("Choose an operation (a-d): ")

        if course_operation == 'a':
            code = input("Enter course code: ")
            name = input("Enter course name: ")
            max_degree = float(input("Enter maximum degree for the course: "))
            credit_hours = int(input("Enter credit hours for the course: "))  
            add_course(code, name, max_degree, credit_hours)

        elif course_operation == 'b':
            code = input("Enter course code to edit: ")
            new_name = input("Enter new course name: ")
            new_max_degree = float(input("Enter new maximum degree for the course: "))
            new_credit_hours = int(input("Enter new credit hours for the course: "))  
            edit_course(code, new_name, new_max_degree, new_credit_hours)

        elif course_operation == 'c':
            code = input("Enter course code to remove: ")
            remove_course(code)

        elif course_operation == 'd':
            display_courses()

        else:
            print("Invalid operation choice.")


    elif user_choice == 3:
        print("(a) Supply grades")
        print("(b) Display student grades")
        grade_operation = input("Choose an operation (a/b): ")

        if grade_operation == 'a':
            course_code = input("Enter course code: ")
            supply_grades(course_code)

        elif grade_operation == 'b':
            course_code = input("Enter course code: ")
            display_student_grades(course_code)

        else:
            print("Invalid operation choice.")

    elif user_choice == 4:
 
          student_code = input("Enter student code: ")
          generate_student_result(student_code)

     

    elif user_choice == 5:
        

    
        print("Statistics:")
        print("(a) Generate Bar Chart")
        print("(b) Generate Pie Chart")
        print("(c) Generate Both")
        print("(d) Back")

        stats_choice = input("Choose a statistics option (a-d): ")

        if stats_choice == 'a':
            generate_bar_chart()
        elif stats_choice == 'b':
            generate_pie_chart()
        elif stats_choice == 'c':
            generate_bar_chart()
            generate_pie_chart()
        elif stats_choice == 'd':
            pass  
        else:
            print("Invalid statistics option.")

    

    elif user_choice == 6:
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please choose a number between 1 and 6.")
if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--demo", action="store_true", help="Generate demo HTML & chart non-interactively")
    p.add_argument("--out", default="./out", help="Output directory for demo artifacts")
    args = p.parse_args()
    if args.demo:
        run_demo(args.out)
    else:
        # existing interactive/menu flow...
        pass

