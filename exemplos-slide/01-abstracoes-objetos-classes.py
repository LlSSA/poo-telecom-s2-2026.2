class Light:
    def __init__(self):
        self.__state = True

    def on(self) -> None:
        self.__state = True

    def off(self) -> None:
        self.__state = False

    def toggle(self) -> None:
        self.__state = not(self.__state)

    def get_state(self) -> bool:
        return self.__state

if __name__ == "__main__":
    luz = Light()
    print(type(luz))