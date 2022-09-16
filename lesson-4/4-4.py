li = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new = [el for el in li if li.count(el) == 1]
print(f'Результат:{new}')
