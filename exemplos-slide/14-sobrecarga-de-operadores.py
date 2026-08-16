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
            self.__z = z

def __add__(self, p_):
    if isinstance(p_, Coord3D):
        res = Coord3D()
        res.x = self.__x + p_.x
        res.y = self.__y + p_.y
        res.z = self.__z + p_.z
        return res