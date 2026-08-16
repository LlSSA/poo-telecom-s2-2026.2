from math import pi
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius_: float):
        self.set_radius(radius_)

    def set_radius(self, radius_: float):
        if radius_ > 0:
            self.__radius = radius_
        else:
            self.__radius = None

    def get_radius(self):
        return self.__radius

    def area(self):
        if self.__radius != None:
            return pi * self.__radius ** 2

class Square(Shape):
    def __init__(self, side_: float):
        self.side = side_

    @property
    def side(self):
        return self.__side
    @side.setter
    def side(self, side_):
        if side_ > 0:
            self.__side = side_
        else:
            self.__side = None

    def area(self):
        if self.side != None:
            return self.side ** 2

