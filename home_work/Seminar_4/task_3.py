# Выведите число π с заданной точностью. Точность выводится в виде десятичной дроби.

#                                     3 -> 3.142

import math

n = int(input("Введите число для заданной точности числа π: "))

print(f'{n} -> {round(math.pi, n)}')
