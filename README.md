# Students Program

## Project Description

The Students Program is a Python-based application designed for efficient management and tracking of students' information, courses, and grades. The application offers a range of features to streamline administrative tasks related to student data, course information, and result generation. Key functionalities include adding, editing, and removing students and courses, supplying grades to students per course, generating result reports, and visualizing data through charts.

### Features

**Manage Students:**
- Add, edit, and remove students' information (code, name, birthdate).
- Display detailed students' information.

**Manage Courses:**
- Add, edit, and remove courses' information (code, name, max degree, credit hours).
- Display comprehensive courses' information.

**Supply Grades:**
- Input grades for students per course.
- Display student grades for a specific course.

**Generate Results:**
- Generate detailed HTML files ("<student-code>.html") containing students' results.
- Calculate course results using the credit hours grading system.

**Statistics:**
- Generate insightful bar charts for students' results per course.
- Generate informative pie charts for course registration.

## File Structure

- **main.py:** Main script to execute the Students Program.
- **students.py:** Module for managing students.
- **courses.py:** Module for managing courses.
- **grades.py:** Module for managing grades.
- **results.py:** Module for generating result reports.
- **statics.py:** Module for generating statistics.
- **students.json:** JSON file storing students' information.
- **courses.json:** JSON file storing courses' information.
- **<course-code>.csv:** CSV files storing grades for each course.
- **<student-code>.html:** HTML files displaying students' results.

## Usage

1. **Clone the Repository:**

2. **Interact with the Program:**
- Choose options (1-6) based on the operation you want to perform.
- Follow on-screen instructions to add/edit/remove students, courses, and grades.

3. **View Results:**
- Students' results are saved as HTML files in the project directory ("<student-code>.html").
- Bar charts for students' results and pie charts for course registration are automatically generated.




