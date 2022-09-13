from itertools import count, cycle

for el in count(3):
    print(el)
    if el == 10:
        break

li = [12, 'привет', 0.7, True]
i = 0
for n in cycle(li):
    i += 1
    if i > 15:
        break
    print(n)
