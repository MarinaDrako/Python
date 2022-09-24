my_str = '1 15 2.7 4 8 6.1 3 12 27 5.2'
summ = 0
with open('text5.txt', 'w+', encoding='utf-8') as f:
    f.write(my_str)
    f.seek(0)
    data = f.read()
    for el in data.split():
        summ += float(el)
print(summ)
