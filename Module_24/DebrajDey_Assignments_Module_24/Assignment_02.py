class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def Perimeter(self):
        return 2 * (self.length + self.width)

    def Area(self):
        return self.length * self.width

    def display(self):
        print(f'The length of rectangle is:  {self.length}')
        print(f'The width of rectangle is:  {self.width}')
        print(f'The perimeter of rectangle is:  {self.Perimeter()}')
        print(f'The area of rectangle is:  {self.Area()}')


my_rectangle = Rectangle(8, 6)

my_rectangle.display()
