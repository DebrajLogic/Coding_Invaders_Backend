class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def Perimieter(self):
        return 2 * (self.length + self.width)

    def Area(self):
        return self.length * self.width

    def display(self):
        print(f'The length of rectangle is:  {self.length}')
        print(f'The width of rectangle is:  {self.width}')
        print(f' The perimeter of rectangle is:  {self.Perimieter()}')
        print(f'The area of rectangle is:  {self.Area()}')


# class Cuboid Inherits class Rectangle
class Cuboid(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def Volume(self):
        return self.length * self.width * self.height


rectangle = Rectangle(8, 6)
rectangle.display()

cuboid = Cuboid(7, 5, 2)
print(f'the volume of my_cuboid is: {cuboid.Volume()}')
