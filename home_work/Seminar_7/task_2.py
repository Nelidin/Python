# Создайте декоратор, повторяющий функцию заданное количество раз.


def our_format(func):
    def decorator(*args):
        for arg in args:
            print(f'{arg} + ', end='')
        print('\b\b= ', end='')
        func(*args)
    return decorator

def repeat(n):
    def operation(func):
        def make(*args):
            for _ in range(n):
                func(*args)
        return make
    return operation

n = int(input('Введите количество повторений функции: '))

@repeat(n)
@our_format
def sum_1(a, b):
    print(a + b)

@repeat(n)
@our_format
def sum_2(a, b, c, d):
    print(a + b + c + d)

print()
sum_1(7, 35)
print()
sum_2(8, 3, 5, 4)
