"""
Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
"""

import random
import pandas as pd


def to_one_hot(column):
    dic_1 = {}
    keys = list(set(column))
    for el in keys:
        dic_1[el] = []
    for i in range(len(column)):
        for j in range(len(keys)):
            if column[i] == keys[j]:
                dic_1[keys[j]].append(1)
            else:
                dic_1[keys[j]].append(0)
    return pd.DataFrame(dic_1)


lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print(data.head())  # здесь и ниже метод .head() применен для сокращения и удобства сравнения вывода
print()
print(to_one_hot(data['whoAmI']).head())
