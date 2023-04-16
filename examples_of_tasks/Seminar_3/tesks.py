import random
import string

# Задача_0: Дан список, заполненный случайными числами от 0 до 10. Определите, является ли сумма всех элементов чётной.

def task_0(): 

    lenght = 7
    # numbers = [0] * lenght
    # for index in range(lenght):
    #     numbers[index] = random.randint(0, 10)
    # print(numbers)

    numbers = [random.randint(0, 10) for el in range(lenght)]
    print(numbers)
    sum = 0
    for index in range(lenght):
        sum += numbers[index]
    print(f'Сумма всех элементов равна {sum}')
    if sum %2 == 0:
        print('Сумма четная')
    else:
        print('Сумма нечетная')

# Задача 1. В списке хранятся сведения о количестве осадков, выпавших за каждый день июня.
# Определите в какой период выпало больше осадков: в первой или второй половине июня.
# Примечание: список заполняется
# случайными числами от 0 до 25.

def task_1():

    days = 30
    numbers = [random.randint(0, 25) for _ in range(days)]
    f_part = numbers[:15]
    s_part = numbers[15:]
    print(numbers)
    print(f_part)
    print(s_part)
    f_sum = 0
    s_sum = 0
    for i in range(len(f_part)):
        f_sum += f_part[i]
        s_sum += s_part[i]
    print(f_sum)
    print(s_sum)
    if f_sum > s_sum:
        print('В первой половине больше')
    elif s_sum > f_sum:
        print('Во второй половине больше')
    else:
        print('Одинаково')

    
# Задача 2. Напишите программу, которая позволит пользователю
# заполнить анкету, последовательно вводя в программу:
# - имя;
# - возраст;
# - хобби;
# - любимое животное.
# После окончания ввода, выводится заполненная анкета.

def task_2():
    
    form = dict(Имя = input('Ваше имя: '), 
                Возраст = input('Ваш возраст: '), 
                Хобби = input('Ваше хобби: '), 
                Любимое_животное = input('Ваше любимое животное: '))
    print()
    for key, value in form.items():
        print("{0}: {1}".format(key,value))

# Задача 3. Напишите скрипт генератора паролей заданной длины, состоящих из латинских букв и чисел.

def task_3(length):
    
    letters_and_digits = string.ascii_letters + string.digits
    password = ''.join(random.sample(letters_and_digits, length))
    print(password)

# task_3(8)


# Задача 4. Ручка стоит – 5 рублей, карандаш – 3 рубля, ластик – 4 рубля.
# Кассир последовательно вводит в программу позиции из чека «ручка», «карандаш», «ластик».
# Ввод заканчивается, когда введено слово «стоп». Определите сумму чека.

def task_4():
    prices = {"ручка": 5, "карандаш": 3, "ластик": 4}
    total = 0
    flag = True
    while flag:
        item = input("Введите товар (ручка, карандаш, ластик) или 'стоп' для завершения: ").lower()
        if item == "стоп":
            flag = False
        elif item in prices:
            total += prices[item]
        else:
            print("Такого товара нет, пожалуйста, введите корректное наименование.")
    return total

total = task_4()
print(f"Сумма чека {total} рублей")

task_4()





# data = open('test.txt', encoding='utf-8')
# text = data.readlines()
# data.close()

# phrase = text[0].split(':')

# bot = {}
# bot[phrase[0]] = phrase[1]
# print(bot)