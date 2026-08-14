class Ponto2D:
    def __init__(self, coord_x = 0, coord_y = 0):
        self.__x = coord_x
        self.__y = coord_y

        @property
        def x(self):
            return self.__x

        @x.setter
        def x(self, valor):
            if isinstance(valor, (int, float)):
                self.__x = valor
            else: 
                raise TypeError("O valor de x tem que ser um número!")

        @y.setter
        def y(self, valor):
            if isinstance(valor, (int, float)):
                self.__y = valor
            else: 
                raise TypeError("O valor de y tem que ser um número!")


        def __add__(self, ponto2):
            novo_x = self.x + ponto2.x
            novo_y = self.y + ponto2.y


            return Ponto2D(novo_x, novo_y)

        def __str__(self):
            return f'({self.x}, {self.y})'



if __name__=='__main__':
    p1 = Ponto2D(2, 9)
    p2 = Ponto2D(3, 16)

    print(p1.x)
    p1.x = 10
    print(p1.x)

    p3 = p2 + p1
    p4 = p3 + 2
    print(p3)
