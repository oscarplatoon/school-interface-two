from classes.staff import Staff
from classes.student import Student

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.objects()
        self.students = Student.objects()
    
    def list_students(self):
        for index, students in enumerate(self.students):
            print(f"{index+1}, {students.name}, {students.school_id}")
            
    def find_student_by_id(self, student_id):
        for index, student in enumerate(self.students):
            if student_id == student.school_id:
                print(student.name)
