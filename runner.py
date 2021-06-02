from classes.school import School

school = School('Ridgemont High')
exit_bool = false
mode = input("\nWhat would you like to do?\nOptions:\n1. List All Students\n2. View Individual Student <student_id>\n3. Add a Student\n4. Remove a Student <student_id>\n5. Quit\n")
print(mode)

while exit_bool not true:
    if mode == '1':
        school.list_students()
    elif mode == '2':
        pass
    elif mode == '3':
        pass
    elif mode == '4':
        pass
    elif mode == '5':
        exit_bool = true
        pass
    