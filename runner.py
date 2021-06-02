from classes.school import School

school = School('Ridgemont High')



mode = input("\nWhat would you like to do?\nOptions:\n1. List All Students\n2. View Individual Student <student_id>\n3. Add a Student\n4. Remove a Student <student_id>\n5. Quit\n")

# print(school.staff)
# print(school.students)

if mode == '1':
    school.list_students()
elif mode == '2':
    student = 'Student Does not exist'
    while student == 'Student Does not exist':
        student_id = input('Enter student id:')
        student = school.find_student_by_id(student_id)
        print(str(student))
else:
    pass


