# grade.py — grade data holder with letter conversion.

class Grade:
    def __init__(self, student: 'Student', course: 'Course', exam: 'Exam', score: float):
        self.student = student
        self.course = course
        self.exam = exam
        self.score = score  # 0..100

    @property
    def letter(self) -> str:
        s = self.score
        if s >= 90: return "A"
        if s >= 80: return "B"
        if s >= 70: return "C"
        if s >= 60: return "D"
        return "F"

    def __repr__(self):
        return f"Grade(student={self.student.name!r}, course={self.course.name!r}, exam={self.exam.title!r}, score={self.score}, letter={self.letter})"