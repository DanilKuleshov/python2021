y = []
n = int(input("Введите число "))
for i in range(2, n + 1):
    p = 0
    for x in range(1, i+1):
        if i % x == 0:
            p += 1
    if p == 2:
        y.append(i)
print("Все простые числа:", y)