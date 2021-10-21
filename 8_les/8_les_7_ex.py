class Complex:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __str__(self):
        return f' {self.re} + {self.im}i'

    def __add__(self, other):
        return f'z1 + z2 = {self.re + other.re} + {self.im + other.im}i'

    def __mul__(self, other):
        return f'z1 * z2 = {self.re * other.re - self.re * other.re}+{self.re * other.im + self.im * other.re}i'


z1 = Complex(1, 1)
print(f'z1 = {z1}')
z2 = Complex(2, 2)
print(f'z2 = {z2}')
print(z1 + z2)
print(z1 * z2)
