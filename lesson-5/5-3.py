f = open('text3.txt', 'r', encoding='utf-8')
content = f.read()
print(f'Содержимое файла:\n{content}')
f.close()
with open('text3.txt', 'r', encoding='utf-8') as f:
    profit = []
    persons = []
    my_strings = f.read().split('\n')
    for i in my_strings:
        i = i.split()
        if float(i[1]) < 20000:
            persons.append(i[0])
        profit.append(i[1])
print(f'Оклад меньше 20000 имеют {persons}, средний оклад {sum(map(float, profit)) / len(profit)}')
