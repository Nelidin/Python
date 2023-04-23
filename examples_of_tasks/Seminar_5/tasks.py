import random

# Задача 0. С помощью анонимной функции найдите в списке на 15 элементов числа, кратные 5. Заполните
# список случайным образом числами от 1 до 100.



def task_0():

    numbers = [random.randint(1, 25) for _ in range (6)]
    print(numbers)
    numbers = list(filter(lambda x: x % 5 == 0, numbers))
    print(numbers)
   

# Задача 1. На вход подаётся четырёхзначное число. Получите список, состоящий из цифр данного числа,
# увеличенных на 10.

# 9650 –> [19, 16, 15, 10]
# 1043 –> [11, 10, 14, 13]

def task_1():

    num = input("Введите число: ")
    numbers = [int(letter) for letter in num]
    print(numbers)
    numbers = list(map(lambda x: x + 10, numbers))
    print(numbers)


# Задача 2. В зоопарк отправили отчёт о новом поступлении
# зверей с ошибкой, в результате которой некоторые данные не
# расшифровались. Расшифруйте данные. Определите, в какой
# клетке находится лев. Номер клетки совпадает с номером
# строки.

# абвгдеёжзийклмнопрстуфхцчшщъыьэюя

def ToBinary(num):
    result = ''
    while num > 0:
        result = str(num % 2) + result
        num //=2
    return '0' * (6 - len(result)) + result

def decoder(code):
    animal = [code[i: i+6] for i in range(0, len(code), 6)] 
    print(animal)

def task_2():
    animals = ['010100001100001001010011001011000000',
                '000001011100001011',
                '001011001111010011',
                '010010010011001111010001001111000111',
                '001100000101000010',
                '001011010001001111001100001001001011',
                '001101010100001100',
                '000001000000010001010010010100001011',
                '000011000101010000000000010001000100',
                '010010001111001101',
                '010010001111000001000000001011000000',
                '011000001001000111']
    
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    alphabet = list(alphabet)
    d = {}
    for i in range(len(alphabet)):
        d[ToBinary(i)] = alphabet[i]
    print(d)

    result = list(map(lambda x: [d[x[i: i+6]] for i in range(0, len(x), 6)] , animals))
    result = list(map(lambda x: ''.join(x), result))
    print(result)


task_2()