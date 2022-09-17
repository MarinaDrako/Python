with open('text2.txt', 'r') as f:
    lines = 1
    for line in f:
        lines += line.count("\n")
        words = len(line.split())
        print(f"Строка {line} содержит слов: {words} ")
    print(f'Количество строк в файле: {lines}.')
