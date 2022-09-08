# список
m = int(input('Введите номер месяца (от 1 до 12): '))
s = ['зима', 'весна', 'лето', 'осень']
if m == 1 or m == 2 or m == 12:
    print(s[0])
elif m == 3 or m == 4 or m == 5:
    print(s[1])
elif m == 6 or m == 7 or m == 8:
    print(s[2])
elif m == 9 or m == 10 or m == 11:
    print(s[3])
else:
    print('Такого месяца не существует')

# словарь
m = int(input('Введите номер месяца (от 1 до 12): '))
di = {'зима': [1, 2, 12], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}
for key in di.keys():
    if m in di[key]:
        print(key)
