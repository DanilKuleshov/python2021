import random
pot = 0

a = int(input("Введите число: "))
a1 = int(input("Введите первоначальное число диапазона: "))
a2 = int(input("Введите конечное число диапазона: "))

b = []
for i in range(0,a):
    b.append(random.randint(a1,a2))

print("Изначальный список:\n",b)

for l in range(0,a-1):
    for j in range(0,a-1):
        if b[j] > b[j+1]:
            pot = b[j]
            b[j] = b[j+1]
            b[j+1] = pot
print("Из метода пузырька мы получим:\n",b)


