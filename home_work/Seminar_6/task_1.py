# Дано натуральное число N. Найдите значение выражения:N + NN + NNN
#                   N может быть любой длины.

#           N = 132: 132 + 132132 + 132132132 = 132264396

def Task_1():

    N = input('Введите число N: ')
    NN = '{}{}'.format(N, N)
    NNN = '{}{}{}'.format(N, N, N)
    res = int(N) + int(NN) + int(NNN)

    print (f'N = {N}: {N} + {NN} + {NNN} = {res}')   

Task_1()