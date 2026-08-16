class Singleton:
    __instance = None

    def __new__(cls, value = None):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.value = value
        return cls.__instance

if __name__ == '__main__':
    a = Singleton("First")
    b = Singleton("Second")
    print(a.value)
    print(b.value)
    print(a is b)
    