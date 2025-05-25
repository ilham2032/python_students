from student import Student

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self,student):
        self.students.append(student)
        print('Added succesfully')

    def rem_student(self,name):
        for student in self.students:
            if student.name == name:
                self.student.remove(student)
                print('Removed succesfully')
            else:
                print('Student is not found')
            
    def show_students(self):
        if student in self.students:
            print(student)
        elif not self.students:
            print('There isnt any student')

    def show_faculities(self):
        all_faculities = []
        for student in self.students:
            all_faculities.append(student.faculity)
        print('Faculities', set{all_faculities})

    def save_to_file(self, filename = 'students.txt'):
        with open(filename, 'w') as f:
            for student in self.students:
                f.write(f'{student.name}, {student.age}, {student.faculity}, {student.birthdate}')
                print('File is saved')
