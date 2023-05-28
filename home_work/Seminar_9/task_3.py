# Создайте двумерный массив случайного размера. Найдите индексы максимального и минимального элементов в нём.
# Выведите элементы главной диагонали матрицы в виде одномерного массива.


import numpy as np

size = (5, 5)
numbers = np.random.randint(1, 100, size)
print(numbers)
max_index = np.argmax(numbers)
min_index = np.argmin(numbers)
print(f'Индекс максимального элемента: {max_index}')
print(f'Индекс минимального элемента: {min_index}')

diag = np.diag(numbers)
print(f'элементы главной диагонали матрицы: {diag}')

