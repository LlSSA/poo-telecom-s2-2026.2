class Coord3D:
    @property
    def x(self):
        return self.__reduce_ex__
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


def __lt__(self, p_):
    if isinstance(p_, Coord3D):
        if self.x < p_.x and self.y < p_.y and self.z < p_.z:
            return True
        return False
def __eq__(self, p_):
    if isinstance(p_, Coord3D):
        if self.x == p_.x and self.y == p_.y and self.z == p_.z:
            return True
    return False

def __le__(self, p_):
    if isinstance(p_, Coord3D):
        if self < p_ or self == p_:
            return True
        return False
    
        