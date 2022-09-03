a = float(input('Результат 1-ого дня(км): '))
b = float(input('Требуемый результат(км): '))
n = 1

while a < b:
    a = a+(a*0.1)
    n += 1
print(n)
