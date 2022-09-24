my_dict = {}
with open('text6.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        data = line.replace('(', ' ').split()
        my_dict[data[0][:-1]] = sum(int(i) for i in data if i.isdigit())
print(my_dict)
