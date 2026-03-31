from services.csv_services import load_students_csv
from services.student_services import (
    add_student,
    list_students,
    search_student,
    update_student,
    delete_student
)

def show_menu():
    print("1. Register new Student")
    print("2. List")
    print("3. Search student")
    print("4. Update student")
    print("5. Delete student")
    print("7. Exit")


def main():
    """Main function — loads data and runs the menu loop."""
    print("Student System")
    print("")

    # Load existing clients from CSV on startup
    students = load_students_csv()
    print(f"{len(students)} client(s) loaded.\n")

    while True:
        show_menu()
        option = input("Select an option (1-7): ").strip()

        if option == "1":
            add_student(students)
        elif option == "2":
            list_students(students)
        elif option == "3":
            search_student(students)
        elif option == "4":
            update_student(students)
        elif option == "5":
            delete_student(students)
        elif option == "7":
            print("\n Goodbye! All data has been saved.")
            break
        else:
            print(" Invalid option. Please choose between 1 and 7.")

# Entry point
if __name__ == "__main__":
    main()
