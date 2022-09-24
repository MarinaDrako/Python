class Cell:

    def __init__(self, amount):
        self.amount = int(amount)

    def __add__(self, other):
        return Cell(self.amount + other.amount)

    def __sub__(self, other):
        if self.amount > other.amount:
            return Cell(self.amount - other.amount)
        else:
            print(f"{self.amount} - {other.amount}: Вычитание ячеек невозможно")

    def __mul__(self, other):
        return Cell(self.amount * other.amount)

    def __truediv__(self, other):
        return Cell(self.amount // other.amount)

    def make_order(self, amount_in_row):

        a = self.amount
        while a > 0:
            for i in range(1, amount_in_row + 1):
                print('*', end='')
                a -= 1
                if a <= 0:
                    break
            print('\n', end='')

    def __str__(self):
        return f"Клетка состоит из {self.amount} ячеек"


c1 = Cell(6)
c2 = Cell(12)
c3 = Cell(5)

print(c1)
print(c1+c2)
print(c1-c2)
print(c2-c3)
print(c1*c2)
print(c2/c3)

c1.make_order(3)
c2.make_order(5)
