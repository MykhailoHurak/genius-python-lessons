# Використати вивчені функції Python:

# Робота зі словниками:
#  1. Cтворити змінну dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'} 
#     та вивести на екран дані, які знаходяться в ключах car та where
#  2. За допомогою функцій keys() і values() вивести на екран ключі та їх значення
#  3. За допомогою функції items() вивести на екран пари ключ - значення

#  =====================================================================

#  1. Cтворити змінну dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'} 
#     та вивести на екран дані, які знаходяться в ключах car та where

dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}

result_1_1 = dict_test.get("car", "---")
print(result_1_1)

result_1_2 = dict_test["where"]
print(result_1_2)

result_1_1 = dict_test.get("model", "---")
print(result_1_1)

#  2. За допомогою функцій keys() і values() вивести на екран ключі та їх значення

result_2_1 = dict_test.keys()
print(result_2_1)
result_2_2 = dict_test.values()
print(result_2_2)

#  3. За допомогою функції items() вивести на екран пари ключ - значення

result_3 = dict_test.items()
print(result_3)