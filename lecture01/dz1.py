import math
from math import sqrt,cos
a = float(input("Введите сторону a: "))
b = float(input("Введите сторону b: "))
y = float(input("Введите угол: "))
c = sqrt((a**2 + b**2) - (2 * a * b * cos(math.radians(y))))
print("c =", c)












