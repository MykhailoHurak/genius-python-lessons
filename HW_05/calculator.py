# Завдання 1: Робота з функціями

# Створіть Python-файл з ім'ям `calculator.py`. 
# У цьому файлі створіть наступні функції:

# 1. `add(a, b)`: Приймає два числа `a` і `b` та повертає їхню суму.
# 2. `subtract(a, b)`: Приймає два числа `a` і `b` та повертає їхню різницю.
# 3. `multiply(a, b)`: Приймає два числа `a` і `b` та повертає їхній добуток.
# 4. `divide(a, b)`: Приймає два числа `a` і `b` і повертає результат ділення `a` на `b`. 
# 
# Пам'ятайте про можливість ділення на нуль і додайте перевірку цього варіанту.

# Після створення цих функцій, напишіть програму, яка імпортує модуль `calculator.py` 
# і використовує його функції для виконання обчислень. 
# Попросіть користувача ввести два числа і операцію (додавання, віднімання, множення або ділення), 
# і виведіть результат обчислення.

def add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")
    return result

def subtract(a, b):
    result = a - b
    print(f"{a} - {b} = {result}")
    return result

def multiply(a, b):
    result = a * b
    print(f"{a} * {b} = {result}")
    return result

def divide(a, b):
    if b == 0:
        print(f"{a} / {b} impossible to count, because number b cannot be 0")
    else:
        result = a / b
        print(f"{a} / {b} = {result}")
        return result