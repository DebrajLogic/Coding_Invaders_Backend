class Person:
    def __init__(self, name, city):
        # I believe the other attribute should be city
        self.name = name
        self.city = city

    def display(self):
        print(f'Person name :  {self.name}')
        print(f'Person city =  {self.city}')


# Class Student Inherits class Person
class Student(Person):
    def __init__(self, name, city, section):
        super().__init__(name, city)
        self.section = section

    def displayStudent(self):
        print(f'Student name :  {self.name}')
        print(f'Student city =  {self.city}')
        print(f'Student section =  {self.section}')


person = Person('Steve', 'San Diego')
person.display()

student = Student('Tony', 'New York', 'Mathematics')
student.displayStudent()
