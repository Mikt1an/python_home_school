# 1
import json
import datetime

def main_json(input_file, output_file):
    """
       Processes student data from a JSON file and generates a report.

       Args:
           input_file (str):
               Path to the source JSON file containing student data.

           output_file (str):
               Path where the generated report JSON file will be saved.

       Returns:
           str:
               Completion status message.

       Description:
           This function:
           - Reads student data from a JSON file
           - Calculates the age of each student at enrollment time
           - Calculates average student age
           - Counts how many students are enrolled in each course
           - Saves the processed statistics into a new JSON report

       Input JSON Structure Example:
           [
               {
                   "name": "John",
                   "birth_date": "15.04.2000",
                   "enrollment_date": "01.09.2020",
                   "courses": ["Python", "Math"]
               }
           ]

       Output JSON Structure Example:
           {
               "max_student": 1,
               "average_age": 20.0,
               "students per courses": {
                   "Python": 1,
                   "Math": 1
               }
           }
       """
    with open(input_file, "r", encoding="utf-8") as json_file:
        students = json.load(json_file)

    max_student = len(students)

    total_age = 0
    curses_count = {}

    for student in students:
        age = calculate_func(student["birth_date"], student["enrollment_date"])
        total_age += age

        for course in student["courses"]:
            curses_count[course] = curses_count.get(course, 0) + 1

    avg_age = total_age / max_student if max_student > 0 else 0

    result = {
        "max_student": max_student,
        "average_age": round(avg_age, 2),
        "students per curses": curses_count
    }

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(result, file, indent=4, ensure_ascii=False)

    return "Completed"

def calculate_func(birth_date, enrollment_date):
    """
        Calculates student's age at the moment of enrollment.

        Args:
            birth_date (str):
                Student birth date in format DD.MM.YYYY
            enrollment_date (str):
                Enrollment date in format DD.MM.YYYY
        Returns:
            int:
                Student age at enrollment.

        Description:
            The function converts string dates into datetime objects
            and calculates the age difference between them.
    """
    birth = datetime.datetime.strptime(birth_date, "%d.%m.%Y").date()
    enrollment = datetime.datetime.strptime(enrollment_date, "%d.%m.%Y").date()

    age = enrollment.year - birth.year
    if (birth.month, birth.day) > (enrollment.month, enrollment.day):
        age -= 1

    return age


rd = main_json("student_courses.json", "student_courses_report.json")
print(rd)