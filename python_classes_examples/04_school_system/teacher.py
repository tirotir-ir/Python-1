# teacher.py — defines the Teacher class.

class Teacher:
    def __init__(self, name: str, subject: str):
        self.name = name
        self.subject = subject
        self.courses = []  # courses taught by this teacher

    def teach(self) -> str:
        return f"{self.name} is teaching {self.subject}"

    def __repr__(self):
        return f"Teacher(name={self.name!r}, subject={self.subject!r})"