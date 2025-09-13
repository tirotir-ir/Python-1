# course.py — defines the Course class.
from typing import List

class Course:
    def __init__(self, name: str, teacher: 'Teacher'):
        self.name = name
        self.teacher = teacher
        self.students: List['Student'] = []
        self.exams: List['Exam'] = []

        # also link course to teacher
        teacher.courses.append(self)

    def add_exam(self, exam: 'Exam'):
        self.exams.append(exam)

    def __repr__(self):
        return f"Course(name={self.name!r}, teacher={self.teacher.name!r})"