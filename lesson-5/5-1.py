f = open('text1.txt', 'w', encoding='utf-8')
while True:
    line = input('Введите текст: \n')
    if not line:
        break
    else:
        f.write(line + '\n')
f.close()
