class A:
    def __init__(self):
        print('Constructor of A')
        super().__init__()
        self.name = 'Class A'
    def __str__(self):
        return self.name
    
class B:
    def __init__(self):
        print('Constructor of B')
        super().__init__()
        self.name = 'Class B'
    def __str__(self):
        return self.name

class C(A, B):
    def __init__(self):
        print('Constructor of C')
        super().__init__()
    def __str__(self):
        return 'C +' + super().__str__()

class D(B, A):
    def __init__(self):
        print('Constructor of D')
        super().__init__()
    def __str__(self):
        return 'D +' + super().__str__()

if __name__ == '__main__':
    a = A()
    print(a)
    b = B()
    print(b)
    c = C()
    print(c)
    print(C.__bases__)
    print(C.__mro__)
    d = D()
    print(d)
    print(D.__bases__)
    print(D.__mro__)