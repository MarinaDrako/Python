def my_func(name, surname, year, city, email, tel):
    print(f'Данные о пользователе: {name}, {surname}, {year}, {city}, {email}, {tel}')


my_func(surname=input('Введите фамилию: '), name=input('Введите имя: '),
        year=input('Введите год рождения: '), city=input('Введите город проживания: '),
        email=input('Введите адрес электронной почты: '), tel=input('Введите номер телефона: '))
