from abc import ABC, abstractmethod
class Polyn(ABC):
    @abstractmethod
    def num_sides(self):

class Triangle(Polygon):
    def num_sides(self):
        return 3

class Square(Polygon):
    def num_sides(self):
        return 4

class Hexagon(Polygon):
    pass

if __name__ == '__main__':
    t = Triangle()
    print('Triangle has {} sides.'.format(t.num_sides()))
    s = Square()
    print('Square has {} sides.'.format(s.num_sides()))
    