# Завдання 2: Створення та імпорт власних модулів

# Створіть власний Python-модуль з ім'ям `utilities.py`. 
# У цьому модулі створіть наступні функції:

# 1. `calculate_average(numbers)`: Приймає список чисел `numbers` і повертає середнє арифметичне цих чисел.
# 2. `find_max(numbers)`: Приймає список чисел `numbers` і повертає найбільше число у списку.

# Після створення цього модуля, створіть інший Python-файл (наприклад, `main.py`), 
# який імпортує модуль `utilities.py` і використовує його функції для обробки списку чисел.

# В `main.py` створіть список чисел та використовуйте функції з модуля `utilities` 
# для знаходження середнього значення та найбільшого числа у списку. 
# Виведіть результати на екран.

import utilities

list_of_numbers_1 = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_of_numbers_2 = [0, 2, 3, 4, 24, 453, 33, 2, -1, 44, 11]

utilities.calculate_average(list_of_numbers_1)
utilities.calculate_average(list_of_numbers_2)

utilities.find_max(list_of_numbers_1)
utilities.find_max(list_of_numbers_2)