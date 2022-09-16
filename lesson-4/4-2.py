li = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new = [li[i] for i in range(1, len(li)) if li[i] > li[i-1]]
print(f'Исходный список: {li}')
print(f'Результат: {new}')
