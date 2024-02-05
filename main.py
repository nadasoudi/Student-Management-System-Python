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
