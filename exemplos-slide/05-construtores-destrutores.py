from Light import Light

class Room:
    def __init__(self):
        self.__light = Light()

    def switch_light(self, state_: bool):
        if self.__light.get_state() != state_:
            self.__light.toggle()

    def is_illuminated(self):
        return self.__light.get_state()


class SquareRoom(Room):
    def __init__(self):
        super().__init__()
        self.__width = 1

    def set_width(self) -> float:
        return self.__width

