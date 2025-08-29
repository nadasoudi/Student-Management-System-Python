import argparse
import os
import csv
import glob

# make matplotlib work in headless/docker environments
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# keep original imports so interactive features still work
from students import *
from courses import *
from grades import *
from results import *   # we will *try* to use calculate_gpa if compatible
from statics import *   # keep menu features intact


# -------- helpers for demo mode (self-contained) --------
def load_all_grades_from_csv() -> dict:
    """
    Scan *.csv files in the repo root. Each CSV is treated as one course.
    Returns: {course_code: {student_code: grade_float}}
    Robust to header/no-header formats:
      - tries DictReader with columns like student* / grade*
      - falls back to first two columns (student_code, grade)
    """
    grades_by_course = {}
    for path in glob.glob("*.csv"):
        course_code = os.path.splitext(os.path.basename(path))[0]
        course_map = {}
        try:
            with open(path, newline="", encoding="utf-8") as f:
                # try header-aware read
                try:
                    reader = csv.DictReader(f)
                    if reader.fieldnames:
                        # detect likely column names
                        student_key, grade_key = None, None
                        for k in reader.fieldnames:
                            lk = k.lower()
                            if ("student" in lk) and ("code" in lk or "id" in lk):
                                student_key = k
                            if ("grade" in lk) or ("score" in lk) or ("mark" in lk):
                                grade_key = k
                        if student_key and grade_key:
                            for row in reader:
                                s = (row.get(student_key) or "").strip()
                                g = (row.get(grade_key) or "").strip()
                                if s and g:
                                    try:
                                        course_map[s] = float(g)
                                    except:
                                        pass
                        else:
                            # fallback: first two columns after header
                            f.seek(0)
                            rr = csv.reader(f)
                            next(rr, None)  # skip header
                            for row in rr:
                                if len(row) >= 2:
                                    s = row[0].strip()
                                    g = row[1].strip()
                                    if s and g:
                                        try:
                                            course_map[s] = float(g)
                                        except:
                                            pass
                    else:
                        # no header -> simple two-col read
                        f.seek(0)
                        rr = csv.reader(f)
                        for row in rr:
                            if len(row) >= 2:
                                s = row[0].strip()
                                g = row[1].strip()
                                if s and g:
                                    try:
                                        course_map[s] = float(g)
                                    except:
                                        pass
                except Exception:
                    # very defensive fallback
                    f.seek(0)
                    rr = csv.reader(f)
                    for row in rr:
                        if len(row) >= 2:
                            s = row[0].strip()
                            g = row[1].strip()
                            if s and g:
                                try:
                                    course_map[s] = float(g)
                                except:
                                    pass
        except FileNotFoundError:
            pass
        if course_map:
            grades_by_course[course_code] = course_map
    return grades_by_course


def safe_calculate_gpa(student_code, grades_by_course, courses):
    """
    Try to call the repo's calculate_gpa if its signature matches.
    Otherwise compute a simple normalized GPA on 4.0 scale:
        per-course contribution = (grade / max_degree) * 4
        GPA = average over courses where student has a grade
    """
    # try repo's calculate_gpa with common signatures
    try:
        return float(calculate_gpa(student_code, grades_by_course, courses))
    except TypeError:
        try:
            return float(calculate_gpa(student_code))
        except Exception:
            pass
    except Exception:
        pass

    # fallback: compute normalized GPA ourselves
    # expect courses to be list of dicts with keys: code, max_degree, credit_hours (optional)
    total = 0.0
    count = 0
    for c in courses:
        code = c.get("code")
        if not code:
            continue
        gmap = grades_by_course.get(code, {})
        # student_code might be str/int; normalize to str keys for CSV map
        scode = str(student_code)
        if scode in gmap:
            try:
                grade = float(gmap[scode])
            except:
                continue
            max_deg = c.get("max_degree") or c.get("maxDegree") or 100.0
            try:
                max_deg = float(max_deg)
            except:
                max_deg = 100.0
            if max_deg > 0:
                total += (grade / max_deg) * 4.0
                count += 1
    return (total / count) if count else 0.0


# -------- Demo (non-interactive) --------
def run_demo(out_dir: str):
    """
    Generate a deterministic HTML summary and a bar chart into out_dir.
    Uses existing JSON/CSV via the repository helpers + local CSV reader.
    """
    os.makedirs(out_dir, exist_ok=True)

    # use repo helpers for JSON
    students = load_students()     # expects students.json
    courses  = load_courses()      # expects courses.json
    # our own CSV aggregator (repo's load_grades requires a course argument)
    grades_by_course = load_all_grades_from_csv()

    # 1) Deterministic HTML summary
    html_path = os.path.join(out_dir, "index.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write("<!doctype html><meta charset='utf-8'><title>Student Summary</title>")
        f.write("<h1>Student Management System — Demo</h1>")
        f.write(f"<p>Students: {len(students)} | Courses: {len(courses)}</p>")
        f.write("<table border='1' cellpadding='6'><tr><th>Code</th><th>Name</th><th>GPA</th></tr>")
        for s in sorted(students, key=lambda x: str(x.get('code', ''))):
            gpa = safe_calculate_gpa(s.get('code'), grades_by_course, courses)
            f.write(f"<tr><td>{s.get('code')}</td><td>{s.get('name')}</td><td>{gpa:.2f}</td></tr>")
        f.write("</table>")

    # 2) Simple bar chart: how many students have a grade per course
    labels, counts = [], []
    for c in sorted(courses, key=lambda x: str(x.get('code', ''))):
        code = c.get('code')
        labels.append(str(code))
        counts.append(len(grades_by_course.get(code, {})))
    plt.figure()
    plt.bar(labels, counts)
    plt.title("Registrations per Course")
    plt.xlabel("Course")
    plt.ylabel("# Students with grade")
    chart_path = os.path.join(out_dir, "registrations_per_course.png")
    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()

    print(f"[demo] wrote: {html_path}")
    print(f"[demo] wrote: {chart_path}")


# -------- Original interactive program, now wrapped --------
def run_interactive():
    while True:
        print("Students Program:")
        print("----")
        print("(1) Add/Edit/Remove students information")
        print("(2) Courses information")
        print("(3) Supply / view  grades to students per course ")
        print("(4) Final result")
        print("(5) Pie")
        print("(6) Exit")

        try:
            user_choice = int(input("Pick a number (1-6): "))
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 6.")
            continue

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


# -------- entry point --------
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true", help="Generate demo HTML & chart non-interactively")
    parser.add_argument("--out", default="./out", help="Output directory for demo artifacts")
    args = parser.parse_args()

    if args.demo:
        run_demo(args.out)
    else:
        run_interactive()
