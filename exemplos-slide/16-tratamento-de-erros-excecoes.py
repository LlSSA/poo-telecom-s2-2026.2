class Rectangle: 
    @property
    def left(self):
        return self.__left
    @left.setter
    def left(self, left_):
        try:
            if left_ > self.right:
                raise ValueError("Invalid value")
            self.__left = left_
        except ValueError:
            print("Left must be < right")
    @property
    def bottom(self):
        return self.__bottom
    @bottom.setter
    def bottom(self, bottom_):
        try:
            if bottom_ > self.top:
                raise ValueError("Invalid value")
            self.__bottom = bottom_
        except ValueError:
            print("bottom must be < top")

    @property
    def right(self):
        return self.__right
    @right.setter
    def right(self, right_):
        try:
            if right_ < self.left:
                raise ValueError("Invalid value")
            self.__right = right_
        except ValueError:
            print("right must be > left")
    @property
    def top(self):
        return self.__top
    @top.setter
    def top(self, top_):
        try:
            if top_ < self.bottom:
                raise ValueError("Invalid value")
            self.__top = top_
        except ValueError:
            print("top must be > bottom")
    def __init__(self):
        self.__left = 0
        self.__botom = 0
        self.__right = 1
        self.__top = 1




