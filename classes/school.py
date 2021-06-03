from classes.staff import Staff
from classes.student import Student

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.objects()
        self.students = Student.objects()

    def list_students(self):
        for student in self.students:
            print(f"{student.name} {student.school_id}")

    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.school_id == student_id:
                return (f"{student.name.upper()}\n.....................\nage: {student.age}\nid: {student.school_id}")

    # return (f"Name: {student.name}, Age: {student.age}, Role: {student.role}, Student ID: {student.school_id}, Password: {student.password}")