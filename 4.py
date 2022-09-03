n = int(input('Введите целое положительное число: '))
i = 0
while n > 0:
    bigger = n % 10
    if bigger >= i:
        i = bigger
    n = n//10
print(i)
