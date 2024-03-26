"""Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()"""

import pandas as pd

# Создаем DataFrame
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Создаем пустой DataFrame для кодирования One-Hot
one_hot_encoded = pd.DataFrame()

# Получаем уникальные значения из столбца
unique_values = data['whoAmI'].unique()

# Проходим по уникальным значениям и создаем новые столбцы для каждого значения
for value in unique_values:
    one_hot_encoded[value] = (data['whoAmI'] == value).astype(int)

# Выводим результат
print(one_hot_encoded.head())

