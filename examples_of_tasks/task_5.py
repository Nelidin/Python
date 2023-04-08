# Напишите программу, которая находит наибольшее и наименьшее число из списка значений

numbers = [1, 6, 9, 10, -3, -4, 5]
print(numbers)
print(numbers[3])
print(f'максимум {max(numbers)}')
print(f'минимум {min(numbers)}')

min_value = numbers[0]
max_value = numbers[0]

for el in numbers:
    print(el)
    if el < min_value:
        min_value = el
    if el > max_value:
        max_value = el

print(f'максимум {max_value}')
print(f'минимум {min_value}')