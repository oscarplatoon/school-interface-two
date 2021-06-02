#runner.py 
from classes.school import School 

school = School('Ridgemont High')

count = 0
while count != 5:

    mode = input("\nWhat would you like to do?\nOptions:\n1. List All Students\n2. View Individual Student\n3. Add a Student\n4. Remove a Student\n5. Quit\n")

    if mode == '1':
        school.list_students()
        count = 1
    elif mode == '2':
        student_id = input('Enter student id:')
        student = school.find_student_by_id(student_id)
        print(str(student))
        count = 2
    elif mode == '5':
        count = 5
        print("Goodbye!")




# Visual
#    1. List All Students
#     2. View Individual Student <student_id>
#     3. Add a Student
#     4. Remove a Student <student_id>
#     5. Quit