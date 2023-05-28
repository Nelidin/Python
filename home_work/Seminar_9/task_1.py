# Дан список элементов. Используя библиотеку NumPy, подсчитайте количество уникальных элементов в нём.

import numpy as np

size = 10
numbers = np.random.randint(1, 10, size)

print(numbers)
uniq_list = np.unique(numbers)

print(f'{uniq_list} - список уникальных элементов')
print("количество уникальных элементов =", len(np.unique(uniq_list)))