# Дано число N. Найти все его делители. Для каждого делителя укажите чётный он или нечётный.
# 	10 -> 10 (чётный), 5(нечётный), 2 (чётный), 1(нечётный)

def check(num):
    if num % 2 == 0:
        return'четное'
    else:
        return'нечетное'

def zadacha0():
    number = int(input('Введите число: '))

    for i in range(1, number+1):
        if number % i == 0:
            print(f'{i} {check(i)}')

# Задача 1. Выведите таблицу истинности для выражения ¬ X ∨ Y.   

def zadacha1():
    print(f'x | y | ¬ X ∨ Y')
    for x in range(0, 2):
        for y in range(0, 2):    
            print(f'{x} | {y} | {int(not x or y)}')


# Задача 2. Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другую.

def zadacha2():
    substring = input('Введите строку: ')
    phrase = input('Введите фразу: ')
    lenght_substr = len(substring)
    lenght_phrase = len(phrase)
    count = 0

    for i in range(lenght_phrase):
        if phrase[i:i+lenght_substr] == substring:
            count +=1
    print(f'В фразе\n{phrase}\ подстрока {substring} встречаетя {count} раз(а)')



# Задача 3. Дано число N. Заполните список длиной N элементами 1, -3, 9, -27, 81, -243...

def zadacha3(n):
    numbers = []
    for el in range(n):
        #print(f'{el} -> {(-3)**el}')
        numbers.append((-3)**el)
    print(numbers)

# Задача 4. Найдите все числа до 10000, у который количество делителей равно 10.

def zadacha4():
    count = 0
    for num in range(1, 10001):
        count_div = 0
        for div in range(1, num+1):
            if num % div == 0:
                count_div += 1
        if count_div == 10: 
            count += 1
            print(num)
    print(f'Кол-во чисел у которых 10 делителей = {count}')

zadacha4()