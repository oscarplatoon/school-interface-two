from classes.staff import Staff
from classes.student import Student

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.objects()
        self.students = Student.objects()

    def list_students(self):
        num = 1
        for student in self.students:
            print(f"{num}. {student.name} {student.school_id}")
            num += 1

    def find_student_by_id(self, student_id):
        for student in self.students:
            if (student.school_id == student_id):
                return student

