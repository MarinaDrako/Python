def my_sum():
    sum_res = 0
    while True:
        li = input('Введите числа через пробел для подсчета суммы и/или "стоп" для завершения работы: ').split()
        for num in li:
            try:
                n = float(num)
                sum_res += n
            except ValueError:
                if num == 'стоп':
                    print(f"Сумма равна {sum_res}. Программа завершена.")
                    return
                else:
                    print(f"Сумма равна {sum_res}. Ошибка ввода данных.")
        print(sum_res)


my_sum()
