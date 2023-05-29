# Задача 3. Постройте диаграмму количества студентов заочной формы обучения за 2019 год по всем регионам, 
#                 в которых общее количество студентов не превышает 10000 за данный год.

#                https://colab.research.google.com/drive/1kbDU9x2D6wYj-NqZRoooBMCFzhEjeyM_

import pandas as pd
import seaborn as sns

df = pd.read_csv('https://minobrnauki.gov.ru/upload/iblock/78d/78d77b235f7b3b14e1ac671e61435311.csv', sep = ';', encoding='cp1251')
df = pd.DataFrame(df, columns= ['Субъект РФ', 'Численность студентов заочная форма, человек, 2019'])
df = df[df['Численность студентов заочная форма, человек, 2019'].between(1,10000)]
plot = sns.barplot(df, x = 'Субъект РФ', y = 'Численность студентов заочная форма, человек, 2019')
plot.set_xticklabels(labels = df['Субъект РФ'], rotation = 90)