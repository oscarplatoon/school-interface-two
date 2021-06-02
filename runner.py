from classes.school import School

school = School('Ridgemont High')

mode = input(f"\nWhat would you like to do?\nOptions:\n1. List All Students\n2. View Individual Student <student_id>\n3. Add a Student\n4. Remove a Student <student_id>\n5. Quit\n")

print(mode)
while mode != "5":
    if mode == '1':
        school.list_students()
    elif mode == '2':
        student_id = input('Enter student id: ')
        student = school.find_student_by_id(student_id)
        printed_student = school.__str__(student)
        exit_var = input(f"Enter 5 to Exit\nHit Enter to continue")
        if exit_var == "5":
            mode = "5"
        else:
            pass    
    else:
        pass 