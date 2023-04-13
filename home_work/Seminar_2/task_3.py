# Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй/

#                     «one» «onetwonine» - o – 2, n – 3, e – 2


def task3():
    substring = input('Введите строку: ')
    phrase = input('Введите фразу: ')
    lenght_substr = len(substring)
    lenght_phrase = len(phrase)
   
    count = 0 
    for i in range(lenght_substr):
        count =0
        for j in range(lenght_phrase):
            if substring[i] == phrase[j]:
                count +=1
        print(f'{substring[i]} - {count}')

task3()
