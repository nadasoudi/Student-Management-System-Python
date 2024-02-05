import tkinter as tk
from tkinter import simpledialog, messagebox

from students import *
from courses import *
from grades import *
from results import *
from statics import *

root = tk.Tk()
root.title("Students Program")


def show_success_message(message):
    messagebox.showinfo("Success", message)

def add_student_gui():
    code = simpledialog.askstring("Add Student", "Enter student code:")
    name = simpledialog.askstring("Add Student", "Enter student name:")
    birthdate = simpledialog.askstring("Add Student", "Enter student birthdate:")
    add_student(code, name, birthdate)
    show_success_message("Student added successfully!")

def edit_student_gui():
    code = simpledialog.askstring("Edit Student", "Enter student code to edit:")
    new_name = simpledialog.askstring("Edit Student", "Enter new student name:")
    new_birthdate = simpledialog.askstring("Edit Student", "Enter new student birthdate:")
    edit_student(code, new_name, new_birthdate)
    show_success_message("Student edited successfully!")

def remove_student_gui():
    code = simpledialog.askstring("Remove Student", "Enter student code to remove:")
    remove_student(code)
    show_success_message("Student removed successfully!")

def display_students_gui():
    display_students()

def add_course_gui():
    code = simpledialog.askstring("Add Course", "Enter course code:")
    name = simpledialog.askstring("Add Course", "Enter course name:")
    max_degree = simpledialog.askfloat("Add Course", "Enter maximum degree for the course:")
    credit_hours = simpledialog.askinteger("Add Course", "Enter credit hours for the course:")
    add_course(code, name, max_degree, credit_hours)
    show_success_message("Course added successfully!")

def edit_course_gui():
    code = simpledialog.askstring("Edit Course", "Enter course code to edit:")
    new_name = simpledialog.askstring("Edit Course", "Enter new course name:")
    new_max_degree = simpledialog.askfloat("Edit Course", "Enter new maximum degree for the course:")
    new_credit_hours = simpledialog.askinteger("Edit Course", "Enter new credit hours for the course:")
    edit_course(code, new_name, new_max_degree, new_credit_hours)
    show_success_message("Course edited successfully!")

def remove_course_gui():
    code = simpledialog.askstring("Remove Course", "Enter course code to remove:")
    remove_course(code)
    show_success_message("Course removed successfully!")

def display_courses_gui():
    display_courses()

def supply_grades_gui():
    course_code = simpledialog.askstring("Supply Grades", "Enter course code:")
    supply_grades(course_code)
    show_success_message("Grades supplied successfully!")

def display_student_grades_gui():
    course_code = simpledialog.askstring("Display Student Grades", "Enter course code:")
    display_student_grades(course_code)

def generate_student_result_gui():
    student_code = simpledialog.askstring("Generate Student Result", "Enter student code:")
    generate_student_result(student_code)
    show_success_message("Result generated successfully!")

def generate_bar_chart_gui():
    generate_bar_chart()
    show_success_message("Bar chart generated successfully!")

def generate_pie_chart_gui():
    generate_pie_chart()
    show_success_message("Pie chart generated successfully!")



buttons = [
    ("Add Student", add_student_gui),
    ("Edit Student", edit_student_gui),
    ("Remove Student", remove_student_gui),
    ("Display Students", display_students_gui),
    ("Add Course", add_course_gui),
    ("Edit Course", edit_course_gui),
    ("Remove Course", remove_course_gui),
    ("Display Courses", display_courses_gui),
    ("Supply Grades", supply_grades_gui),
    ("Display Student Grades", display_student_grades_gui),
    ("Generate Student Result", generate_student_result_gui),
    ("Generate Bar Chart", generate_bar_chart_gui),
    ("Generate Pie Chart", generate_pie_chart_gui),
    ("Exit", root.destroy)
]


for text, command in buttons:
    tk.Button(root, text=text, command=command).pack()

root.mainloop()