li = input('Введите элементы списка: ').split()

for i in range(0, len(li)-1, 2):
    li[i], li[i+1] = li[i+1], li[i]
    print(li)