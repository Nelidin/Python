# Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5. Используйте для решения лямбда-функцию.

#                                         2, 3, 4, 6, 7, 8 -> 6, 7, 8

import random

def Task_1():

    numbers = [random.randint(1, 10) for _ in range (6)]
    print(numbers, end = " -> ")
    numbers = list(filter(lambda x: x > 5, numbers))
    print(numbers)

Task_1()