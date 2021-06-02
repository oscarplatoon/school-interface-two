from classes.staff import Staff
from classes.student import Student

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.objects()
        self.students = Student.objects()

    def list_students(self):
        for i, obj in enumerate(self.staff):
            print (f"{i+1}. {obj.name} {obj.employee_id}")
     
        for i, obj in enumerate(self.students):
            print (f"{i+1}. {obj.name} {obj.school_id}")
    
    def find_student_by_id(self, student_id):
        for obj in self.students:
            if obj.school_id == student_id:
                # print(obj.name)
                return obj
        return 'Student Does not exist'