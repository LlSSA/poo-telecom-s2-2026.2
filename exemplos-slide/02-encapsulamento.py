from Light import Light

class SquareRoom:
    def __init__(self):
        self.__width = 1
        self.__light = Light()

    def get_width(self) -> float:
        return self.__width

    def set_width(self, width_:float) -> None:
        if width_ > 0:
            self.__width = width_

    def switch_light(self, state_: bool):
        if self.__light.get_state() != state_:
            self.__light.toggle()

    def is_illuminated(self):
        return self.__light.get_state()