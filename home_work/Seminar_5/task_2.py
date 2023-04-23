# Дан список случайных чисел. Создайте список, в который попадают числа, описывающие случайную возрастающую последовательность. 
# Порядок элементов менять нельзя.

#                             [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [2, 7] или [4, 6, 7] и т.д.

import random

def Task_2():

    numbers = [1, 5, 2, 3, 4, 6, 1, 7]
    print(numbers, end = " => ")
    y = [random.randint(1, 6) for _ in range (1)]
    numbers = list(filter(lambda x: x >= y[0], numbers))
    print(numbers)
  
Task_2()