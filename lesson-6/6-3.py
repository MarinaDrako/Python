class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'Полное имя сотрудника: {self.name + " " + self.surname}'

    def get_total_income(self):
        return f'Доход с учетом премии: {sum(self._income.values())} BYN.'


p1 = Position('Иван', 'Соколов', 'Водитель', 600, 300)
print(p1.get_full_name())
print(p1.position)
print(p1.get_total_income())
