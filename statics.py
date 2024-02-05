
import matplotlib.pyplot as plt
from results import load_students, load_courses, load_grades, calculate_gpa

def generate_bar_chart():
    students = load_students()
    courses = load_courses()

    for course in courses:
        course_code = course["code"]
        gpa_list = []

        for student in students:
            student_code = student["code"]
            gpa = calculate_gpa(student_code)
            gpa_list.append(gpa)

        
        plt.bar([student["name"] for student in students], gpa_list)
        plt.xlabel("Students")
        plt.ylabel("GPA")
        plt.title(f"GPA Distribution for Course {course_code}")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()

        
        plt.savefig(f"bar_chart_{course_code}.png")

        plt.show()

def generate_pie_chart():
    courses = load_courses()
    course_labels = [course["name"] for course in courses]
    course_sizes = [len(load_grades(course["code"])) for course in courses]

    
    plt.pie(course_sizes, labels=course_labels, autopct='%1.1f%%', startangle=140)
    plt.title("Course Registration Distribution")
    plt.axis('equal')  

    
    plt.savefig("pie_chart_course_registration.png")

    
    plt.show()

if __name__ == "__main__":
    generate_bar_chart()
    generate_pie_chart()
