from classes.staff import Staff
from classes.student import Student

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.objects()
        self.students = Student.objects()


    def list_students(self):
        for k in self.students:
            print(f"1. {k.name} {k.school_id}")

    def __str__(self):
        return f'{self.name}\n---------\nage: {self.age}\nid: {self.student_id}'

    def find_student_by_id(self, student_id):
        for i in self.students:
            if i.school_id == student_id:
                print(i.__str__())

