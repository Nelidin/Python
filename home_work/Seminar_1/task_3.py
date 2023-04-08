# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат
#                                 точек в этой четверти (x и y).

#                                     1 -> x > 0, y > 0

numbers = int(input('Введите номер четверти: '))

if numbers >= 1 and numbers <= 4:
    if numbers == 1:
        print(f'{numbers} -> x > 0, y > 0')
    if numbers == 2:
        print(f'{numbers} -> x < 0, y > 0')
    if numbers == 3:
        print(f'{numbers} -> x < 0, y < 0')
    if numbers == 4:
        print(f'{numbers} -> x > 0, y < 0')
else:
    print('Такой четверти не существует!')
