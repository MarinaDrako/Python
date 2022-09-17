rus = ["Один", "Два", "Три", "Четыре"]
new_trans = []

with open('text4.txt', 'r', encoding='utf-8') as f_eng:
    content = f_eng.readlines()
    print(content)
    n = 0
    for line in content:
        a = line.find(' ')
        b = line[:a]
        repl = line.replace(b, rus[n])
        n += 1
        new_trans.append(repl)
with open('text4_new.txt', 'w', encoding='utf-8') as f_rus:
    f_rus.writelines(new_trans)
