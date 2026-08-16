class Square:
    def __init__(self, side=1):
        self.side = side
    @property
    def side(self):
        return self.__side
    @side.setter
    def side(self, value):
        if value > 0:
            self.__side = value
        else:
            raise ValueError('side must > 0')

if __name__ == '__main__':
    s1 = Square()
    s2 = Square(2)
    s3 = Square(side = 3)
    print('side1 =', s1.side)
    print('side2 = ', s2.side)
    print('side3 =', s3.side)