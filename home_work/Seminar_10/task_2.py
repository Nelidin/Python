# Задача 2. Постройте диаграмму с данными о численности студентов дневной формы обучения южного федерального округа 
#                                               за 2017 год.
                  
#                   https://colab.research.google.com/drive/1kbDU9x2D6wYj-NqZRoooBMCFzhEjeyM_


import pandas as pd
import seaborn as sns

df = pd.read_csv('https://minobrnauki.gov.ru/upload/iblock/78d/78d77b235f7b3b14e1ac671e61435311.csv', sep = ';', encoding='cp1251')
df = pd.DataFrame(df, columns= ['Субъект РФ', 'Численность студентов, очная форма, человек, 2017'])
df = df.iloc[2:20]
plot = sns.barplot(df, x = 'Субъект РФ', y = 'Численность студентов, очная форма, человек, 2017')
plot.set_xticklabels(labels = df['Субъект РФ'], rotation = 90)