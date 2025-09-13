# exam.py — Exam for a course; can assign scores to students.
from typing import Dict

class Exam:
    def __init__(self, title: str, course: 'Course', max_score: float = 100.0):
        self.title = title
        self.course = course
        self.max_score = max_score
        self.scores: Dict['Student', float] = {}  # map Student -> raw score

        # register with course
        course.add_exam(self)

    def assign_score(self, student: 'Student', score: float) -> str:
        if student not in self.course.students:
            return f"{student.name} is not enrolled in {self.course.name}."
        if not (0 <= score <= self.max_score):
            return f"Score must be between 0 and {self.max_score}."
        self.scores[student] = score
        return f"Recorded {score} for {student.name} on '{self.title}'"

    def get_score(self, student: 'Student'):
        return self.scores.get(student, None)

    def __repr__(self):
        return f"Exam(title={self.title!r}, course={self.course.name!r}, max_score={self.max_score})"