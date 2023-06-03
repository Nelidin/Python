import numpy as np

# Задача 1. Проверьте, существует ли связь между данными, приведёнными в таблице.Выполните задание с помощью библиотеки numpy.

# [56, 37, 48, 45, 46, 43, 41, 45, 47, 48, 57, 63]
# [66, 46, 46, 54, 57, 51, 52, 54, 57, 54, 68, 72]
# [89, 67, 65, 77, 79, 68, 74, 75, 77, 77, 91, 96]


def task_1():
    nums_f = [56, 37, 48, 45, 46, 43, 41, 45, 47, 48, 57, 63]
    nums_s = [66, 46, 46, 54, 57, 51, 52, 54, 57, 54, 68, 72]
    nums_t = [89, 67, 65, 77, 79, 68, 74, 75, 77, 77, 91, 96]

    matrix = [nums_f, nums_s, nums_t]
    result = np.corrcoef(matrix)
    print(result)


# Дан массив случайных чисел. Создайте его с помощью NumPy. Определите его среднее арифметическое.
#  На ввод подаётся число. Определите ближайший по значению к нему элемент массива.
# [1.2, 4.2, 5.6, 7.1] -> 4.525
# 6.1 -> 5.6

def task2():
    size = 10
    numbers = np.random.randint(10, 100, size)
    print(numbers)

    mean = np.mean(numbers)
    print(f'среднее арифметическое {mean}')

    
    num = int(input('\nВведите число: '))
    dist = [np.abs(el - num) for el in numbers]
    print(f'дистанции {dist}')
    min_dist = np.min(dist)
    print(f'минимальное расстояние {min_dist}')
    index_min_dist = dist.index(min_dist)
    print(f'индекс минимального расстояния {index_min_dist}')

    print(f'ближайший элемент к {num} равен {numbers[index_min_dist]}')

# Задайте квадратную матрицу, состоящую из случайных чисел. Найдите самый часто
# встречающийся элемент в этой матрице.

def task_3():
    size = (4, 4)
    numbers = np.random.randint(1, 10, size)
    print(numbers)

    uniq_list, uniq_counts = np.unique(numbers, return_counts=True)
    print(f'уникальные элементы {uniq_list}')
    print(f'их количество       {uniq_counts}')
    index_max = np.argmax(uniq_counts)
    print(index_max)
    print(f'Элемент {uniq_list[index_max]} встречает {uniq_counts[index_max]}')

# Дан двумерный массив, заполненный нулями и единицами. Определите, есть ли в нём нулевые столбцы.

def task_4():
    size = (3, 6)
    numbers = np.random.randint(0, 2, size)
    print(numbers)
    
    result = numbers.any(axis=0)
    print(result)
    result = ~result
    print(result)

    if True in result:
        print('В матрице есть столбец, состоящий из нулей')
    else:
        print('Нулевых столбцов нет')

task_4()