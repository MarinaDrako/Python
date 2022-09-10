# с помощью оператора **
def my_func(x, y):
    return 1 / x ** abs(y)
    # return x ** y


print(my_func(2, -3))


# с помощью цикла
def my_func1(x1, y1):
    res = 1
    i = 1
    while i <= abs(y1):
        res = res * x1
        i += 1
    return 1/res


print(my_func1(float(input('Введите первое значение (действительное положительное число): ')),
               int(input('Введите второе значение (целое отрицательное число): '))))
