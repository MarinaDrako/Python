li = input('Введите несколько слов: ').split()
for i, el in enumerate(li, 1):
    print(f'{i}.{el[0:10]}')
