my_list = [7, 5, 3, 3, 2]
print(my_list)
new_el = int(input('Введите новый элемент рейтинга: '))
if new_el == 1 or new_el == 2:
    my_list.append(new_el)
elif new_el == 3:
    my_list.insert(4, new_el)
elif new_el == 4 or new_el == 5:
    my_list.insert(2, new_el)
elif new_el == 6 or new_el == 7:
    my_list.insert(1, new_el)
elif new_el == 8 or new_el >= 8:
    my_list.insert(0, new_el)
else:
    print('Вы ввели не натуральное число. Попробуйте ещё раз.')
print(my_list)
