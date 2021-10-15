import random

a = int(input("Введите число: "))
a1 = int(input("Введите первоначальное число диапазона: "))
a2 = int(input("Введите конечное число диапазона: "))

b = []
for i in range(0,a):
    b.append(random.randint(a1,a2))

print(b)
