import calendar


class Date:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def set_date(cls, day_month_year):

        my_date = []
        for el in day_month_year.split('-'):
            if el != '-':
                my_date.append(el)

        return cls(day=int(my_date[0]), month=int(my_date[1]), year=int(my_date[2]))

    def __str__(self):
        return f'Date is: {self.day}-{self.month}-{self.year}'

    @staticmethod
    def validate(day, month, year):

        end_month_day = 28 or 29 or 30 or 31

        if month in [1, 3, 5, 7, 8, 10, 12]:
            end_month_day = 31
        elif month in [4, 6, 9, 11]:
            end_month_day = 30
        elif month == 2:
            if calendar.isleap(year):
                end_month_day = 29
            else:
                end_month_day = 28
        else:
            print("Invalid Month")

        if 1 <= day <= end_month_day:
            print("Valid Day")
        else:
            print("Invalid Day")

        if 1900 <= year <= 2200:
            return f'Year is valid'
        else:
            return f'Invalid year'


date = '04-10-2022'
today = Date.set_date(date)
print(today)
print(Date.validate(20, 10, 2022))
print(Date.validate(32, 12, 2020))
print(Date.validate(32, 13, 3020))
print(today.set_date('01-01-2023'))
print(Date.validate(31, 2, 2025))
print(Date.validate(28, 2, 2025))
