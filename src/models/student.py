
class Student:

    def __init__(self, id, name, age, program, status="active"):
        self.id = id
        self.name = name
        self.age = age
        self.program = program        # "database", "frontend", "backend","fullstack"
        self.status = status    # "active ", "inactive"

    def to_dict(self):
        """Converts the students object into a dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "program": self.program,
            "status": self.status
        }

    @staticmethod
    def from_dict(data):
        """Creates a students object from a dictionary."""
        return Student(
            id=int(data["id"]),
            name=data["name"],
            age=int(data["age"]),
            program=data["program"],
            status=data["status"]
        )

    def __str__(self):
        """Returns a readable string representation of the students."""
        return (f"ID: {self.id} | Name: {self.name} | Age: {self.age} | "
                f"Program: {self.program} | Status: {self.status}")