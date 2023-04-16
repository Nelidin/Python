# Дано натуральное число N. Напишите метод, который вернёт список простых множителей числа N и количество этих множителей.

#                                                             60 -> 2, 2, 3, 5
#                                                             4 - множителя


def multiplier():

    num = int(input("Введите натуральное число: "))
    res = []
    count = 0
    n = num
    i = 2

    while i <= num:

        if num % i == 0:
            res.append(i)
            num //= i
            count += 1                 
        else:
            i += 1
                   
    print(f"{n} -> {res}\n{count} - множителя")

multiplier()
