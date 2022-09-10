def my_func():
    try:
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))
        return a/b
    except ZeroDivisionError:
        print('Делить на ноль нельзя!')


print(f'Результат: {my_func()}')
