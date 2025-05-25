class Student:
    def __init__(self,name,age,faculity,birthdate):
        self.name = name
        self.age = age
        self.faculity = faculity
        self.birthdate = birthdate

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}, Faculity: {self.faculity}, Birth: {self.birthdate}'