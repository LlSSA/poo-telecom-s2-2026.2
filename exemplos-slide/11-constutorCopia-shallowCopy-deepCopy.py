import copy

class Point2D:
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x_):
        try:
            if not(isinstance(x_, (int, float))):
                raise ValueError('x must be a number.')
            else:
                self.__x = x_
        except ValueError:
            print('x must be a number.')

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y_):
        try:
            if not (isinstance(y_, (int, float))):
                raise ValueError('y must be a number.')
            else:
                self.__y = y_
        except ValueError:
            print('y must be a number.')

    def __init__(self, x_ = 0, y_ = 0):
        self.x = x_
        self.y = y_


class Circle:
    @property
    def center(self):
        return self.__center
    @center.setter
    def center(self, center_):
        try:
            if not(isinstance(center_, Point2D)):
                raise ValueError("Center must be a Point2D.")
            else:
                self.__center = center_

        except ValueError:
            print("Something went wrong")
    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self, radius_):
        try:
            if not(isinstance(radius_, (int, float))):
                raise ValueError("Radius must be a number.")
            elif radius_ <= 0:
                raise ValueError("Radius must be positive.")
            else:
                self.__radius = radius_
        except ValueError:
            print('Something went wrong')

def __init__(self, x_ = 0, y_ = 0, radius_ = 1, clone_ = None):
    try:
        if isinstance(clone_, Circle):
            self.radius = clone_.radius
            self.center = clone_.center
        elif radius_ > 0:
            self.radius = radius_
            self.radius = radius_
            self.center = Point2D(x_, y_)
        else:
            raise ValueError('Something went wrong')
    except ValueError:
        print('Something went wrong')


if __name__ == '__main__':
    c1 = Circle(x_ = 1, y_=1, radius_=2)
    c2 = c1

    c1.radius = 5
    print('Bind: Changes 1, impacts both')
    print('c1.r:', c1.radius, 'c1.x:', c1.center.x, 'c1.y:', c1.center.y)
    print('c2.r:', c2.radius, 'c2.center.x', 'c2.y', c2.center.y)

    c2 = copy.copy(c1)
    c1.radius = 3
    c1.center.x = -1
    c1.center.y = -2
    print('Shallow: Changes 1, still impacts both')
    print('c2.r:', c2.radius, 'c2.x:', c2.center.x, 'c2.y:', c2.center.y)

    c2 = copy.deepcopy(c1)
    c1.radius = 4
    c1.center.x = -3
    c1.center.y = -4
    print('Deep: Changes 1, changes 1')
    print('c1.r:', c1.radius, 'c1.x:', c1.center.x, 'c1.y:', c1.center.y)
    print('c2.r:', c2.radius, 'c2.x:', c2.center.x, 'c2.y:', c2.center.y)