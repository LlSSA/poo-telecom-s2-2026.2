class Coord3D:
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x_):
        if isinstance(x_, (int, float)):
            self.__x = x_
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y_):
        if isinstance(y_, (int, float)):
            self.__y = y_
    @property
    def z(self):
        return self.__z
@z.setter
def z(self, z_):
    if isinstance(z_, (int, float)):
        self.__z = z_

class Coord3D:
    def __init__(self, clone_ = None):
        if isinstance(clone_ = None):
            if isinstance(clone_, Coord3D):
                self.x, self.y, self.z = clone_.x, clone_.y, clone_.z
            else:
                self.x, self.y, self.z = 0.0, 0.0, 0.0

    def __str__(self):
        res = str(self.x) + ','
        res += str(self.y) + ','
        res += str(self.z)
        return res

