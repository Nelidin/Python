# Задача 1. Дан список случайных элементов. Проверьте, что все его элементы уникальны.
                               
#                                 Решение задач:
#                                 [7, 2, 4, 1, 6] –> да
#                                 [7, 2, 4, 2, 6] -> нет

import random
import collections

def task_1():

    numbers = [7, 2, 4, 1, 6]     
    if len(numbers) == len(set(numbers)):
        print(f'{numbers} -> да')
    else:
        print(f'{numbers} -> нет')


# Задача 2. Даны два случайных пятизначных числа. Определить, состоят ли они из одних и тех же цифр.

# 72426, 27624 –> да
# 44444, 44441 -> нет

def task_2():

    number_f = 12555
    number_s = 51255
    
    num_f_dict = dict((i, str(number_f).count(i)) for i in set(str(number_f)))
    print(num_f_dict)
    num_s_dict = dict((i, str(number_s).count(i)) for i in set(str(number_s)))    
    print(num_s_dict)

    if num_f_dict == num_s_dict:
        print('Наборы цифр одинаковы')
    else:
        print('Наборы цифр одинаковы')


# Задача 3. Напишите программу вычисления арифметического
# выражения заданного строкой. Используйте операции +,-,/,*.
# приоритет операций стандартный.
# а) Решите задачу для одного действия;
# б) Дополнительное задание. Решите задачу для нескольких
# действий;
# в) Решите задачу средствами python.

# 2+2 => 4
# 1+2*3 => 7 

def task_3():
    expression = input('Введите выражение: ')
    expression = expression.replace('-', '+-')
    expression = expression.replace('/', '* 1/')
    print(expression)

    if '+' in expression:
        expression = expression.split('+')
        print(int(expression[0] + int(expression[1])))
    # elif '-' in expression:
    #     expression = expression.split('-')
    #     print(int(expression[0] - int(expression[1])))
    elif '*' in expression:
        expression = expression.split('*')
        print(int(expression[0] * int(expression[1])))
    # elif '/' in expression:
    #     expression = expression.split('/')
    #     print(int(expression[0] / int(expression[1])))
    

# Задача 4. Имеется 1000 рублей. Бык стоит – 100
# рублей, корова – 50 рублей, телёнок – 5 рублей.
# Сколько быков, коров и телят можно купить на все
# эти деньги, если всего надо купить 100 голов
# скота?

def task_4():
    budget = 1000
    
    bull_price = 100
    cow_price = 50
    calf_price = 5
    bulls_count = budget // bull_price
    cow_count = budget // cow_price
    calf_count = budget // calf_price
    
    for bulls in range(bulls_count+1):
        for cows in range(cow_count+1):
            for calf in range(calf_count+1):
                if bulls + cows + calf == 100 and \
                    bulls * bull_price + cows * cow_price + calf * calf_price <= 1000 and\
                    bulls * bull_price + cows * cow_price + calf * calf_price >= 500:
                    print(f'Быков: {bulls}; Коров: {cows}; Телят: {calf}')
       

task_4()