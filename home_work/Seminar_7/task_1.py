# Создайте пользовательский аналог метода map().

def square(x):
    return x ** 2

def my_map(func, numbers):    
    result = []
    for num in numbers:
        result.append(func(num))
    return result
numbers = [1, 2, 3, 4, 5]

print(list(my_map(square, numbers)))
