from math import sqrt
from abc import ABC, abstractmethod
class Shape(ABC):
    def __init__(self): pass
    @abstractmethod
    def area(self): pass

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
    for s in [Square(), EquilateralTriangle()]:
        if isinstance(s, Shape):
            print('area = ', s.area) # Different behaviors