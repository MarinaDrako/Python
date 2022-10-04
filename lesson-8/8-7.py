class MyComplex:
    def __init__(self, real, imag=0):
        self.__complex = complex(real, imag)

    def __add__(self, other):
        if isinstance(other, MyComplex):
            other = other.__complex

        complexx = self.__complex + other
        return MyComplex(complexx.real, int(complexx.imag))

    def __mul__(self, other):
        if isinstance(other, MyComplex):
            other = other.__complex

        complexx = self.__complex * other
        return MyComplex(complexx.real, int(complexx.imag))

    def __str__(self):
        return self.__complex.__str__()


c1 = MyComplex(1, -4)
c2 = MyComplex(3, 2)

print(c1)
print(c2)

print(c1 + c2)
print(c1 * c2)
