from math import sqrt
class Shape:
    def __init__(self):
        self.__area = 0

    @property
    def area(self):
        return self.__area

class Square(Shape):
    def __init__(self, side=1):
        self.side = side
    @property
    def side(self):
        return self.__side
    @side.setter
    def side(self, value):
        if isinstance(value, (int, float)) and value > 0:
            self.__side = value
        else:
            raise ValueError('side must be a positive number')
    @property
    def area(self):
        return self.side**2

class EquilateralTriangle(Shape):
    def __init__(self, side=1):
        self.side = side

    @property
    def side(self):
        return self.__side
    @side.setter
    def side(self, value):
        if isinstance(value, (int, float)) and value > 0:
            self.__side = value
        else:
            raise ValueError('side must be a positive number')
    @property
    def area(self):
        return self.side**2*sqrt(3)/4

if __name__ == '__main__':
    shapes = [Shape(), Square(), EquilateralTriangle()]
    for s in shapes:
        print('area=', s.area)