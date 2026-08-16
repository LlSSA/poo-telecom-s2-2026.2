class Stringfyable:
    def __init__(self, content):
        self.content = content
    @property
    def content(self):
        return self.__content
    @content.setter
    def content(self, value):
        if isinstance(value, str):
            self.__content = value
        else:
            try:
                self.__content = value.__str__()
            except Exception:
                print('value must at least implement __str__')

    def __add__(self, value):
        if isinstance(value, str):
            content = self.content + value
        else:
            try:
                content = self.content + value.__str__()
            except Exception:
                print('value must at least implement __str__')
        return Stringfyable(content)
    
def __str__(self):
    return self.__content

if __name__ == '__main__':
s1 = Stringfyable(20)
s2 = Stringfyable('/')
s3 = Stringfyable([1, 2, 3])
s4 = Stringfyable('Hello World')
print(s1 + '/' + 10 + s2 + s3 + '/' + 15.5 + '/' + s4 + '/' + 10)