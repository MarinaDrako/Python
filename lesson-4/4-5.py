from functools import reduce
li = [el for el in range(100, 1001) if el % 2 == 0]
print(f'Результат: {reduce((lambda x, y: x * y),li)}')
