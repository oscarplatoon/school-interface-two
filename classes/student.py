import csv
import os.path
from classes.person import Person

class Student(Person):

    def __init__(self, name, age, password, role, school_id):
        super().__init__(name, age, password, role)
        self.school_id = school_id

    @classmethod
    def objects(cls):
        students = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/students.csv")
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                students.append(Student(**dict(row)))
        return students
    
    @classmethod
    def empty(cls):
        #def __init__(self, name, age, password, role, school_id):
        return cls("Not Found", -1, "xx", "Student", -1)
        
    def __str__(self):
        output = self.name.upper()
        output += f"\n---------------\nage: {self.age}\nid: {self.school_id}"
        return output
