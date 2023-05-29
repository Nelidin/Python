# Задача 1. Найдите, какая область центрального федерального округа имела наибольшую численность студентов 
#                                   вечерней формы обучения в 2015 году.

#               https://colab.research.google.com/drive/1Yt5e4L7kiGa51VgUIPC8bNjA4QJ1p_9E

import pandas as pd

df = pd.read_csv('https://minobrnauki.gov.ru/upload/iblock/78d/78d77b235f7b3b14e1ac671e61435311.csv', sep = ';', encoding='cp1251')
df = pd.DataFrame(df, columns= ['Субъект РФ', 'Численность студентов очно-заочная (вечерняя) форма, человек, 2015'])
df = df.iloc[2:20]
max_value = df['Численность студентов очно-заочная (вечерняя) форма, человек, 2015'].max()
df[df['Численность студентов очно-заочная (вечерняя) форма, человек, 2015'] == max_value]