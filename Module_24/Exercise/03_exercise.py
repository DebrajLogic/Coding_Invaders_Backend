class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.__roll_no = roll_no

    def get_roll_no(self):
        return self.__roll_no

    def set_roll_no(self, new_roll_no):
        if (new_roll_no > 100):
            print("Invalid roll no. Please set correct roll number")
            return
        self.__roll_no = new_roll_no

    def show(self):
        print(f'Student Name: {self.name}, Roll no: {self.__roll_no}')


new_student = Student('Angelina', 80)

new_student.set_roll_no(90)

new_student.show()
