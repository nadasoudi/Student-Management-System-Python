Students Program
Project Description
The Students Program is a Python-based application designed to manage and track students' information, courses, and grades. It provides functionalities such as adding, editing, and removing students and courses, supplying grades to students per course, generating result reports, and visualizing data through charts.

Features
Manage Students:

Add, edit, and remove students' information (code, name, birthdate).
Display students' information.
Manage Courses:

Add, edit, and remove courses' information (code, name, max degree, credit hours).
Display courses' information.
Supply Grades:

Input grades for students per course.
Display student grades for a specific course.
Generate Results:

Generate HTML files ("<student-code>.html") containing students' results.
Calculate course results using the credit hours grading system.
Statistics:

Generate bar charts for students' results per course.
Generate pie charts for course registration.

#File Structure#
main.py: Main script to run the Students Program.
students.py: Module for managing students.
courses.py: Module for managing courses.
grades.py: Module for managing grades.
results.py: Module for generating results.
statics.py: Module for generating statistics.
students.json: JSON file to store students' information.
courses.json: JSON file to store courses' information.
<course-code>.csv: CSV files to store grades for each course.
<student-code>.html: HTML files to display students' results.


Interact with the Program:

Choose options (1-6) based on the operation you want to perform.
Follow on-screen instructions to add/edit/remove students, courses, and grades.
View Results:

Students' results are saved as HTML files in the project directory ("<student-code>.html").
Bar charts for students' results and pie charts for course registration are generated.
