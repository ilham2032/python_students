from student import Student, StudentManager

manager = StudentManager()

while True:
    print('1. Add srudent')
    print('2. Remove Student')
    print('3. Show students')
    print('4. Show student faculities')
    print('5. Save to file')
    print('Exit the program')

    option = input('Choose the option...')


    if option == '1':
        name = input('Name:')
        age = int(input('Age:'))
        faculity = input('FAculity:')
        day = int(input('Day: '))
        month = int(input('Month:'))
        year = int(input('Year:'))
        birthdate = (day, month, year)
        student = Student(name, age, facility, birthdate)
        manager.add_student(student)

    elif option == '2':
        name = input('Write the name of the student....')
        manager.rem_student(name)

    elif option == '3':
        manager.show_students()

    elif option == '4':
        manager.show_faculities()
    
    elif option == '5':
        manager.save_to_file()

    elif option == '6':
        print('Leaving the program..')
        break

    else:
        print('Choice the right option please')