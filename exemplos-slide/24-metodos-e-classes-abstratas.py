from abc import ABC, abstractmethod
class Polygon(ABC):
    @abstractmethod
    def num_sides(self):
        pass
    @property
    @abstractmethod
    def sides(self):
        pass
    @sides.setter
    @abstractmethod
    def sides(self, lengths_):
        pass
    
class Triangle(Polygon):
    def __init__(self):
        self.__num_sides = 3
        self.sides = [1]*self.__num_sides
    def num_sides(self):
        return self.__num_sides
    @property
    def sides(self):
        return self.__lenghts
    @sides.setter
    def sides(self, lenghts_):
        if isinstance(lenghts_, list) and len(lenghts_) == self.num_sides():
            self.__lenghts = lenghts_
if __name__ == '__main__':
    t =Triangle()
    print('Triangle has {} sides: {}.' .format(t.num_sides(), t.sides))