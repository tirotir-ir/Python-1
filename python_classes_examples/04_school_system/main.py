# main.py — demo runner for the mini school system.
# Shows Students, Teachers, Courses, Exams, and Grades working together.

from teacher import Teacher
from course import Course
from student import Student
from exam import Exam
from grade import Grade

def transcript(student: Student):
    print(f"\nTranscript for {student.name}:")
    rows = []
    for course in student.courses:
        for ex in course.exams:
            sc = ex.get_score(student)
            if sc is not None:
                g = Grade(student, course, ex, sc)
                rows.append((course.name, ex.title, sc, g.letter))
    if not rows:
        print("  No scores yet.")
    else:
        for cname, ex_title, sc, letter in rows:
            print(f"  {cname:10s} | {ex_title:12s} | score: {sc:5.1f} | letter: {letter}")

if __name__ == "__main__":
    # Teachers
    t_math = Teacher("Mr. Smith", "Math")
    t_sci  = Teacher("Ms. Johnson", "Science")

    # Courses
    algebra = Course("Algebra", t_math)
    biology = Course("Biology", t_sci)

    # Students
    alice = Student("Alice", 16)
    bob   = Student("Bob", 17)

    # Enrollments
    print(alice.enroll(algebra))
    print(bob.enroll(biology))
    print(alice.enroll(biology))

    # Teachers in action
    print(t_math.teach())
    print(t_sci.teach())

    # Exams
    mid_algebra = Exam("Midterm", algebra, max_score=100)
    quiz_bio    = Exam("Quiz 1", biology, max_score=20)

    # Record scores
    print(mid_algebra.assign_score(alice, 92))
    print(quiz_bio.assign_score(alice, 17))  # Alice enrolled in Biology too
    print(quiz_bio.assign_score(bob, 15))

    # Show transcripts
    transcript(alice)
    transcript(bob)