from classes.staff import Staff
from classes.student import Student

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.objects()
        self.students = Student.objects()


    def list_students(self):
        print(f'\n\n')
        for i,student in enumerate(self.students):
            print(f'{i+1}. {student.name} {student.school_id}')

    def find_student_by_id(self, id):
        for i,student in enumerate(self.students):
            if id == student.school_id:
                print(f'\n{student}')
                break

