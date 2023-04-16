
import random

def change_element(numbers, index):
   return numbers[:index] + (random.randint(1, 100), ) + numbers[index + 1:]

def calculate(n1,n2):
   return n1 + n2, n1 - n2, n1 * n2, n1/n2

# Задача 0. Создайте кортеж. Запишите в него 10 случайных чисел.

def task_0():

   numbers = tuple(random.randint(1, 10) for _ in range(10))

   print(numbers)

# Задача 1:
# Создайте кортеж, заполненный случайными числами.
# Напишите метод, который заменяет элемент в
# кортеже по заданному индексу другим случайным
# числом.

def task_1():

   numbers = tuple(random.randint(1, 100) for _ in range(10))
   index = 4

   print(numbers)
   numbers_new = change_element(numbers, index)
   print(numbers_new)
   print(type(numbers_new))


# Задача 2:
# На вход подаются два числа. Напишите метод, который вернёт
# сумму, разность, произведение и частное этих чисел.

def task_2():

   num_f = 9
   num_s = 3

   summ, raznost, umnozhenie, delenie = calculate(num_f, num_s)
   print(summ, raznost, umnozhenie, delenie)


# Задача 3:
# 15 мин
# Сгенерируйте список случайных чисел от 1 до 20,
# состоящий из 10 элементов. Удалите из списка
# дубликаты уже имеющихся элементов. Определите,
# сколько элементов было удалено.
# [1, 2, 9, 5, 2, 18, 3, 5, 13, 2] -> [1, 2, 9, 5, 18, 3, 13]
# Удалено элементов: 3

def task_3():

   numbers = [random.randint(1,20) for _ in range(10)]
   print(numbers)
   length = len(numbers)
   numbers = list(set(numbers))
   print(numbers)
   print(f'Элементов было удалено: {length - len(numbers)}')

# Задача 4. Актёров разделили на списки по трём качествам
# «умные», «красивые», «сильные». На главную роль нужен
# актёр обладающий всеми тремя качествами. Определите,
# сколько есть претендентов на главную роль.
# Красивые: Илья Федор Семен Олег Лев Антон Артем Боря Стас Марк Ян
# Умные: Илья Георгий Лев Демьян Антон Владислав Боря Стас Марк Влад
# Сильные: Федор Георгий Олег Демьян Артем Елисей Боря Стас Влад

def task_4():

   beautiful = set("Илья Федор Семен Олег Лев Антон Артем Боря Стас Марк Ян".split())
   brainy = set("Илья Георгий Лев Демьян Антон Владислав Боря Стас Марк Влад".split())
   strong = set("Федор Георгий Олег Демьян Артем Елисей Боря Стас Влад".split())

   top = beautiful.intersection(brainy, strong)
   print(top)


task_4()