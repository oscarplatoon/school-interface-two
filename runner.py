from classes.school import School

school = School('Ridgemont High')



mode = input("\nWhat would you like to do?\nOptions:\n1. List All Students\n2. View Individual Student <student_id>\n3. Add a Student\n4. Remove a Student <student_id>\n5. Quit\n")

# print(school.staff)
# print(school.students)

if mode == '1':
    school.list_students()
else:
    pass


