from classes.school import School

school = School('Ridgemont High')

#Main loop
while(True):
    selection = input("\nWhat would you like to do?\nOptions:\n1. List All Students\n2. View Individual Student <student_id>\n3. Add a Student\n4. Remove a Student <student_id>\n5. Quit\n")
    print("")
    if selection == '1':
        school.list_students() 
    elif selection == '2':
        student_id = input('Enter student id: ')
        print("")
        student = school.find_student_by_id(student_id)
        print(str(student))
    elif selection == '5':
        break
    
