products = int(input("Введите количество позиций товара: "))
n = 1
my_dict = []
my_list = []
my_analysis = {}
while n <= products:
    my_dict = dict({'Название': input('Введите название: '), 'Цена': input('Введите цену: '),
                    'Количество': input('Введите количество: '), 'Ед': input('Введите единицы измерения: ')})
    my_list.append((n, my_dict))
    n += 1
    my_analysis = dict({'название': [my_dict.get('Название')], 'цена': [my_dict.get('Цена')],
                        'количество': [my_dict.get('Количество')], 'ед': [my_dict.get('Ед')]})
print(my_list)
print(my_analysis)
