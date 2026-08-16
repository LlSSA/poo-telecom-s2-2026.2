from typing import Any

def greetings(name: str) -> str:
    return f'Hello! My name is {name}!'

class Person:
    def __init__(self, name: str):
        self.name = name

    def greet(self):
        print(greetings(self.name))


if __name__ == '__main__':
    John = Person('John Snow')
    John.greet()

