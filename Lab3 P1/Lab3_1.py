import math


class Rational:
    def __init__(self, numerator=1, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    @property
    def numerator(self):
        return self.__numerator

    @numerator.setter
    def numerator(self, numerator):
        if not isinstance(numerator, int):
            raise ValueError
        self.__numerator = numerator

    @property
    def denominator(self):
        return self.__denominator

    @denominator.setter
    def denominator(self, denominator):
        if not isinstance(denominator, int) and denominator:
            raise ValueError
        self.__denominator = denominator

    def __str__(self):
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd
        fraction = f''
        if self.numerator < 0 and self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1
        if self.numerator != 0:
            fraction += f'{self.numerator}'
        else:
            fraction += f'0'
        if self.denominator != 1:
            fraction += f' / {self.denominator}'
        return fraction


    def __add__(self, other):
        if isinstance(other, Rational):
            return Rational(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator * other.denominator )
        if isinstance(other, int):
            return Rational(self.numerator + other*self.denominator, self.denominator)

    def __radd__(self, other):
        if isinstance(other, Rational):
            return Rational(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator * other.denominator )
        if isinstance(other, int):
            return Rational(self.numerator + other*self.denominator, self.denominator)

    def __iadd__(self, other):
        if isinstance(other, Rational):
            return Rational(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator * other.denominator )
        if isinstance(other, int):
            return Rational(self.numerator + other*self.denominator, self.denominator)

    def __sub__(self, other):
        if isinstance(other, Rational):
            return Rational(self.numerator * other.denominator - other.numerator * self.denominator, self.denominator * other.denominator )
        if isinstance(other, int):
            return Rational(self.numerator - other*self.denominator, self.denominator)

    def __mul__(self, other):
        if isinstance(other, Rational):
            return Rational(self.numerator * other.numerator, self.denominator * other.denominator)
        if isinstance(other, int):
            return Rational(self.numerator * other, self.denominator)

    def __floordiv__(self, other):
        if isinstance(other, Rational):
            return Rational(self.numerator * other.denominator, self.denominator * other.numerator)
        if isinstance(other, int):
            return Rational(self.numerator, self.denominator * other)

    def __truediv__(self, other):
        if isinstance(other, Rational):
            return Rational(int((self.numerator * other.denominator) / (self.denominator * other.numerator)), 1)
        if isinstance(other, int):
            return Rational(int(self.numerator / (self.denominator * other)), 1)

    def __gt__(self, other):
        if isinstance(other, Rational):
            return (self.numerator * other.denominator) > (other.numerator * self.denominator)
        if isinstance(other, int):
            return (self.numerator // self.denominator) > other

    def __lt__(self, other):
        if isinstance(other, Rational):
            return (self.numerator * other.denominator) < (other.numerator * self.denominator)
        if isinstance(other, int):
            return (self.numerator // self.denominator) < other

    def __eq__(self, other):
        if isinstance(other, Rational):
            return (self.numerator * other.denominator) == (other.numerator * self.denominator)
        if isinstance(other, int):
            return (self.numerator // self.denominator) == other

    def __ge__(self, other):
        if isinstance(other, Rational):
            return (self.numerator * other.denominator) >= (other.numerator * self.denominator)
        if isinstance(other, int):
            return (self.numerator // self.denominator) >= other

    def __le__(self, other):
        if isinstance(other, Rational):
            return (self.numerator * other.denominator) <= (other.numerator * self.denominator)
        if isinstance(other, int):
            return (self.numerator // self.denominator) <= other

x = Rational(4,2)
print(x)
y = Rational(3,5)
print(y)
print(x+y)
print(x+2)
print(x-y)
print(x-2)
print(x*y)
print(x*2)
print(x//y)
print(y//2)
print(x/y)
print(y/2)
print(x>y)
print(y>2)
x += y
print(x)



