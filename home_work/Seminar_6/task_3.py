# Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11.


def farey( n, asc=True ):
    if asc: 
        a, b, c, d = 0, 1, 1, n
    else:
        a, b, c, d = 1, 1, n-1, n
    print(f"{a}/{b}")
    while (asc and c <= n) or (not asc and a > 0):
        k = (n + b) // d
        a, b, c, d = c, d, k*c - a, k*d - b
        print(f"{a}/{b}")

farey(11)