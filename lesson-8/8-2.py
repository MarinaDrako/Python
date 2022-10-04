class MyError(Exception):

    def __init__(self, txt):
        self.txt = txt


a = input('Введите числитель: ')
b = input('Введите знаменатель: ')

try:
    a = float(a)
    b = float(b)
    if b == 0:
        raise MyError('Делить на ноль нельзя!')
except (ValueError, TypeError, MyError) as err:
    print(err)
else:
    print(a/b)
finally:
    print('Завершено')
