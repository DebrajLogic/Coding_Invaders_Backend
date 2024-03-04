class Employee:
    def __init__(self, name, dept, salary):
        self.name = name
        self.dept = dept
        self.__salary = salary.replace('$', '')

    def show(self):
        print(f'Name:  {self.name} Salary: {self.__salary} Dept: {self.dept}')


new_employee = Employee('Steve Rogers', 'IT', ' $10000')

new_employee.show()
