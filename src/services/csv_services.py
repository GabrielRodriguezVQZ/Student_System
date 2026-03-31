import csv
import os
from models.student import Student

CSV_FILE = "src/data/list_students.csv"
COLUMNS = ["id", "name", "age", "program", "status"]


def save_students_csv(students):
    """Saves the full list of Client objects to the CSV file."""
    file = open(CSV_FILE, "w", newline="", encoding="utf-8")
    writer = csv.DictWriter(file, fieldnames=COLUMNS)
    writer.writeheader()
    for student in students:
        writer.writerow(student.to_dict())
    file.close()
    print(" Data saved to CSV.")


def load_students_csv():
    """Loads clients from the CSV file and returns a list of Client objects."""
    students = []

    if not os.path.exists(CSV_FILE):
        return students

    file = open(CSV_FILE, "r", newline="", encoding="utf-8")
    reader = csv.DictReader(file)
    for row in reader:
        student = Student.from_dict(row)
        students.append(student)
    file.close()

    return students