# Создайте двумерный массив, размером 5х5. Определите, есть ли в нём одинаковые строки.

import numpy as np

def realization_1():

    size = (5, 5)
    numbers = np.random.randint(0, 2, size)
    print(f'{numbers}\n')
    result = np.corrcoef(numbers)
    print(result)
   

def realization_2():
    size = (5, 5)
    numbers = np.random.randint(0, 2, size)
    print(f'{numbers}\n')
    unique_rows = np.unique(numbers, axis=0)       
    if len(numbers) == len(unique_rows):
        print('Массив состоит из разных строк!')
    else:
        print('Одинаковые строки есть!')

realization_2()