class Vehicle:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price
        self.speed = 150
        self.gear = 6

    def max_speed(self):
        print(f'Vehicle max speed is {self.speed}')

    def gears(self):
        print(f'Vehicle have {self.gear} gear')

    def show(self):
        print(f'Details: {self.name} {self.color} {self.price}')


# class Car Inherits class Vehicle
class Car(Vehicle):
    def __init__(self, name, color, price):
        super().__init__(name, color, price)
        self.speed = 240
        self.gear = 7

    def max_speed(self):
        print(f'Car max speed is {self.speed}')

    def gears(self):
        print(f'Car change {self.gear} gear')


# class Bus also Inherits class Vehicle
class Bus(Vehicle):
    def __init__(self, name, color, price):
        super().__init__(name, color, price)
        self.speed = 200
        self.gear = 8

    def max_speed(self):
        print(f'Bus max speed is {self.speed}')

    def gears(self):
        print(f'Bus change {self.gear} gear')


# car object from class Car
car = Car('BMW', 'Red', '20000')
car.show()
car.max_speed()
car.gears()

# bus object form class Bus
bus = Bus('Tavera x1', 'white', '75000')
bus.show()
bus.max_speed()
bus.gears()
