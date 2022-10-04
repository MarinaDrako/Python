class OnlyNumbers(Exception):

    def __init__(self, txt):
        self.txt = txt


my_list = []
while True:
    user_input = input("Введите число или 'stop' для выхода: ")
    if user_input == "stop":
        break
    try:
        if not user_input.isdigit():
            raise OnlyNumbers(f"'{user_input}' не является числом! В список не добавится!")
        my_list.append(int(user_input))
    except OnlyNumbers as err:
        print(err)

print(my_list)
