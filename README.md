# Student System

A console-based student management system for a University, built with Python. It allows you to register, search, update, and delete clients, with automatic data persistence using CSV files.

---

##  Project Structure

```
gym_management_system/
│
├── main.py                  # Entry point — runs the main menu loop
│
├── data/
│   └── list_students.csv          # Auto-generated file where client data is stored
│
├── models/
│   └── students.py            # Client class (data model)
│
└── services/
    ├── students_service.py    # Business logic — CRUD operations
    └── csv_service.py       # Data persistence — read/write CSV file

```

---

##  Requirements

- Python 3.x
- No external libraries required — uses only Python built-in modules (`csv`, `os`)

---

##  How to Run

Navigate into the project folder and run:

```bash
python3 main.py
```

The program will automatically load any existing client data from the CSV file on startup.

---

##  Features

| Option | Feature               | Description                                      |
|--------|-----------------------|--------------------------------------------------|
| 1      | Register new Student  | Adds a new client with all their information     |
| 2      | List all Student      | Displays a formatted table of all clients        |
| 3      | Search Student        | Finds a client by ID or name                     |
| 4      | Update Student        | Edits an existing client's information           |
| 5      | Delete Student        | Removes a client after confirmation              |
| 7      | Exit                  | Closes the program                               |

---

##  Client Data Fields

Each client record contains the following fields:

| Field    | Type    | Description                                                    |
|----------|---------|----------------------------------------------------------------|
| `id`     | Integer | Unique auto-generated identifier                               |
| `name`   | String  | Full name of the client                                        |
| `age`    | Integer | Age of the client (1–120)                                      |
| `program`| String  | Membership plan: `database`, `frontend`, `backend`, `fullstack`|
| `status` | String  | Current status: `active` or `inactive`                         |

---

##  Data Persistence

Students data is saved automatically to `data/list_students.csv` every time a change is made (create, update, or delete). When the program starts, it loads all existing data from the file, so no information is lost between sessions.


---

##  Module Responsibilities

| File                         | Responsibility                                           |
|------------------------------|----------------------------------------------------------|
| `main.py`                    | Menu loop, user interaction, program entry point         |
| `models/student.py`          | Client class with `to_dict()` and `from_dict()` methods  |
| `services/student_service.py`| All CRUD functions with input validation                 |
| `services/csv_service.py`    | Open, read, and write the CSV file                       |

---

##  Validations

The system includes basic input validation for all operations:

- Name and required fields cannot be empty
- Age must be a number between 1 and 120
- Plan must be one of the accepted values
- Status must be `active` or `inactive`
- ID must be a valid integer when searching, updating, or deleting
- All errors are handled with `try/except` to prevent crashes

---

##  Author

Gabriel Rodriguez