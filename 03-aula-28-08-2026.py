from math import gcd

class Fracao:
    def __init__(self, num=1, den=1):
        self.num = num
        self.den = den
    
    def _reduce(self, num, den):
        if num !=0 and den !=0:
            mdc = gcd(num, den)
            num = num // mdc
            den = den // mdc
            return num, den
        else:
            return 0, 1
        
        
    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, value):
        if isinstance(value, int):
            self.__num = value
        else:
            raise TypeError('num deve ser inteiro.')

    @property
    def den(self):
        return self.__den

    @den.setter
    def den(self, value):
        if isinstance(value, int):
            if value != 0:
                self.__den = value
            else:
                raise ValueError('den deve ser diferente de zero.')
        else:
            raise TypeError('num deve ser inteiro.')

    def __add__(self, other):
        if isinstance(other, Fracao):
            num = self.num * other.den + other.num * self.den
            den = self.den * other.den

            if num != 0: 
                mdc = gcd(num, den)
                num = num // mdc
                den = den // mdc
                return Fracao(num, den)
            else: 
                return Fracao(0, 1)

        else: 
            raise TypeError('Só se pode somar fração com fração')

    def __sub__(self, other):
            if isinstance(other, Fracao):
                num = self.num * other.den - other.num * self.den
                den = self.den * other.den

                if num != 0: 
                    mdc = gcd(num, den)
                    num = num // mdc
                    den = den // mdc
                    return Fracao(num, den)
                else: 
                    return Fracao(0, 1)

            else: 
                raise TypeError('Só se pode subtrair fração com fração')

            
    def __mul__(self, other):
            if isinstance(other, Fracao):
                num = self.num * other.num
                den = self.den * other.den

                if num != 0: 
                    mdc = gcd(num, den)
                    num = num // mdc
                    den = den // mdc
                    return Fracao(num, den)
                else: 
                    return Fracao(0, 1)
            else: 
                raise TypeError('Só se pode multiplicar fração por fração')
            
    def __floordiv__(self, other):
        if isinstance(other, Fracao):
            if other.num == 0:
                raise ZeroDivisionError('Divisão por zero')
                
            num = self.num * other.num
            den = self.den * other.den
            if num != 0: 
                mdc = gcd(num, den)
                num = num // mdc
                den = den // mdc
                return Fracao(num, den)
            else: 
                return Fracao(0, 1)
        else: 
            raise TypeError('Só se pode multiplicar fração por fração')
            
    def __eq__(self, other):
        return self.num == other.num and self.den == other
        
    def __lt__(self, other):
        return self.num * other.num < self.den == other

    def __str__(self):
        return f'{self.num}/{self.den}'
        

if __name__ == "__main__":
    f1 = Fracao(1, 5)
    print(f1)
    f2 = Fracao(2, 5)
    print(f2)
    f3 = f1 + f2
    print(f3)
    
# def test_1():
    #import Fracao as f
    #f1 = f.Fracao(1, 2)
    #f2 = f.Fracao(1, 3)
    
    #assert f1 + f2 == f.Fracao(5, 6)