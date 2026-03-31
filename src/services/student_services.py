from models.student import *
from services.csv_services import *

VALID_PROGRAM = ["database", "frontend", "backend","fullstack"]
VALID_STATUSES = ["active", "inactive"]

def generate_id(students):
    """Generates a unique ID based on the highest existing ID."""
    if len(students) == 0:
        return 1
    highest_id = 0
    for student in students:
        if student.id > highest_id:
            highest_id = student.id
    return highest_id + 1

def add_student(students):
    """Asks the user for data and registers a new client."""
    print("\n Register new student")
    print("-" * 35)

    # Name
    name = input("Student name: ").strip()
    if name == "":
        print(" Name cannot be empty.")
        return

    # Age
    try:
        age = int(input("Age: "))
        if age <= 0 or age > 120:
            print(" Invalid age.")
            return
    except ValueError:
        print(" Age must be a number.")
        return

    # Plan
    print(f"Available Program: {' / '.join(VALID_PROGRAM)}")
    program = input("Program type: ").strip().lower()
    if program not in VALID_PROGRAM:
        print(f" Invalid program. Choose from: {', '.join(VALID_PROGRAM)}")
        return

    new_student = Student(
        id=generate_id(students),
        name=name,
        age=age,
        program=program,
        status="active"
    )

    students.append(new_student)
    save_students_csv(students)
    print(f"Student '{name}' registered with ID {new_student.id}.")


def list_students(students):
    """Displays all registered student in a formatted table."""
    print("\n List")
    print("-" * 60)

    if len(students) == 0:
        print("No students registered yet.")
        return

    print(f"{'ID':<5} {'Name':<22} {'Age':<6} {'Program':<12} {'Status'}")
    print("-" * 60)
    for student in students:
        print(f"{student.id:<5} {student.name:<22} {student.age:<6} {student.program:<12} {student.status}")
    print("-" * 60)
    print(f"Total: {len(students)} student(s)")


def search_student(students):
    """Searches for Student by ID or name."""
    print("\n search student")
    print("-" * 35)
    term = input("Enter ID or name to search: ").strip().lower()

    results = []
    for student in students:
        if str(student.id) == term or term in student.name.lower():
            results.append(student)

    if len(results) == 0:
        print("No student found.")
        return

    print(f"\n{len(results)} result(s) found:\n")
    for student in results:
        print(f"  ID     : {student.id}")
        print(f"  Name   : {student.name}")
        print(f"  Age    : {student.age}")
        print(f"  Program   : {student.program}")
        print(f"  Status : {student.status}")
        print("  " + "-" * 30)

def update_student(students):
    print("\n  Update Student")
    print("-" * 35)

    try:
        search_id = int(input("Student ID to update: "))
    except ValueError:
        print(" ID must be a number.")
        return

    found = None
    for student in students:
        if student.id == search_id:
            found = student
            break

    if found is None:
        print(" No client found with that ID.")
        return

    print(f"\nEditing: {found.name}  (leave blank to keep current value)\n")

    new_name = input(f"Name [{found.name}]: ").strip()
    if new_name != "":
        found.name = new_name

    new_age = input(f"Age [{found.age}]: ").strip()
    if new_age != "":
        try:
            age_int = int(new_age)
            if 0 < age_int <= 120:
                found.age = age_int
            else:
                print("  Invalid age, keeping previous value.")
        except ValueError:
            print("  Invalid age, keeping previous value.")

    print(f"Available program: {' / '.join(VALID_PROGRAM)}")
    new_program = input(f"Program [{found.program}]: ").strip().lower()
    if new_program != "":
        if new_program in VALID_PROGRAM:
            found.program = new_program
        else:
            print("  Invalid plan, keeping previous value.")

    print(f"Available statuses: {' / '.join(VALID_STATUSES)}")
    new_status = input(f"Status [{found.status}]: ").strip().lower()
    if new_status != "":
        if new_status in VALID_STATUSES:
            found.status = new_status
        else:
            print("  Invalid status, keeping previous value.")

    save_students_csv(students)
    print(" Stuent updated successfully.")

def delete_student(students):
    """Deletes a client by ID after confirmation."""
    print("\n  DELETE CLIENT")
    print("-" * 35)

    try:
        delete_id = int(input("Client ID to delete: "))
    except ValueError:
        print(" ID must be a number.")
        return
    
    found = None
    for student in students:
        if student.id == delete_id:
            found = student
            break

    if found is None:
        print("No student found with that ID.")

    confirm = input(f"Delete '{found.name}'? (y/n): ").strip().lower()
    if confirm == "y":
        students.remove(found)
        save_students_csv(students)
        print("Student deleted successfully.")
    else:
        print("Operation cancelled.")