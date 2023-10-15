#Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
#Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

#import random
#lst = ['robot'] * 10
#lst += ['human'] * 10
#random.shuffle(lst)
#data = pd.DataFrame({'whoAmI':lst})
#data.head()


import pandas as pd

df = pd.DataFrame({'column':['a','b','c','a','b','c','a']})
unique_values = df['column'].unique()

one_hot_df = pd.DataFrame(0, index=df.index, columns=unique_values)

for value in unique_values:
        one_hot_df.loc[df['column'] == value, value] = 1

print(one_hot_df)

