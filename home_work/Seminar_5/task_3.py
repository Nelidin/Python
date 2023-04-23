# Задайте список случайных чисел от 1 до 10. Посчитайте, сколько всего совпадающих элементов есть в списке. 
# Удалите все повторяющиеся элементы.

# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают. 
# Список уникальных элементов [1, 4, 2, 3, 6, 7]

import random

def Task_3():

    numbers = [random.randint(1, 10) for _ in range (8)]
    print(numbers, end = " => ")
    
    length = len(numbers)
    numbers = list(set(numbers))

    print(f'{length - len(numbers)} элемента совпадают')
    print(f'Список уникальных элементов: \n{numbers}')   

Task_3()