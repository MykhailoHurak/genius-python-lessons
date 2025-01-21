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

def calculate_average(numbers):
    total = 0
    for number in numbers:
        total = total + number
    average = total / len(numbers)

    # print(f"total = {total}")
    # print(f"len(numbers) = {len(numbers)}")
    print(f"numbers = {numbers}")
    print(f"average = {average}")
    print("-------")

    return average

def find_max(numbers):
    max_number = numbers[0]
    for num in numbers:
        if num > max_number:
            max_number = num
    print(f"numbers = {numbers}")
    print(f"max_number = {max_number}")
    print("-------")
    return max_number        

# list_of_numbers = [1, 2, 3, -10, -100, 122, 4, 5, 6, 7, 8, 9, 10, 4, 3]
# list_of_numbers_2 = [0, 2, 3, 4, 24, 453, 33, 2, -1, 44, 11]
# calculate_average(list_of_numbers_2)
# find_max(list_of_numbers)