# 3-6
def int_func(words):
    return words.title()


print(int_func('hello everybody'))

# 3-7
li = input('Введите слова латинскими буквами: ').split()
s = ' '.join((map(str, li)))

print(int_func(s))
