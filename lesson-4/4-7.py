n = int(input('Найдём факториал числа: '))


def fact():
    count = 1
    while count <= n:
        yield count
        count += 1


f = 1
my_list = []
for el in fact():
    if f > 10000:
        break
    else:
        my_list.append(el)
        f = f * el
print(my_list)
print(f)
