# student.py — defines the Student class.
from typing import List

class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.courses: List['Course'] = []  # forward reference

    def enroll(self, course: 'Course') -> str:
        if course not in self.courses:
            self.courses.append(course)
            course.students.append(self)
            return f"{self.name} enrolled in {course.name}"
        return f"{self.name} is already enrolled in {course.name}"

    def list_courses(self):
        return [c.name for c in self.courses]

    def __repr__(self):
        return f"Student(name={self.name!r}, age={self.age})"