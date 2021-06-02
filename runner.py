from classes.school import School

school = School('Ridgemont High')

while(True):
    mode = input("\nWhat would you like to do?\nOptions:\n1. List All Students\n2. View Individual Student <student_id>\n3. Add a Student\n4. Remove a Student <student_id>\n5. Quit\n")

    if mode == '1':
        school.list_students()

    elif mode == '2':
        school_id = input('Enter school id: ')
        student = school.find_student_by_id(school_id)
        print(str(student))
    elif mode == '3':
        pass
    elif mode == '4':
        pass
    elif mode == '5':
        break
    else:
        print(mode)