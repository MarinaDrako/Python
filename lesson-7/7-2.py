from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @abstractmethod
    def consumption(self):
        pass

    def __str__(self):
        return str(self.param)


class Coat(Clothes):

    @property
    def consumption(self):
        return round(self.param / 6.5 + 0.5, 2)


class Suit(Clothes):

    @property
    def consumption(self):
        return round(self.param * 2 + 0.3, 2)


a = Coat(46)
b = Suit(1.70)
print(a)
print(a.consumption)
print(b.consumption)
