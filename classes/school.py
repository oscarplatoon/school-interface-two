from classes.staff import Staff
from classes.student import Student

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.objects()
        self.students = Student.objects()

    def list_students(self):
        for index, student in enumerate(self.students):
            print(f"{index+1}. {student.name} {student.school_id}")
    
    def find_student_by_id(self, school_id):
        for student in self.students:
            if school_id == student.school_id:
                return student
        return(None)
