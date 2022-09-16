from sys import argv

print(f'Выработка в часах: {argv[1]} ставка в час: {argv[2]} премия: {argv[3]}')
path, p1, p2, p3 = argv
print(f'Заработная плата сотрудника: {int(p1)*int(p2)+int(p3)}')
