# Завдання 1: Робота з функціями

# Створіть Python-файл з ім'ям `calculator.py`. 
# У цьому файлі створіть наступні функції:

# 1. `add(a, b)`: Приймає два числа `a` і `b` та повертає їхню суму.
# 2. `subtract(a, b)`: Приймає два числа `a` і `b` та повертає їхню різницю.
# 3. `multiply(a, b)`: Приймає два числа `a` і `b` та повертає їхній добуток.
# 4. `divide(a, b)`: Приймає два числа `a` і `b` і повертає результат ділення `a` на `b`. 
# Пам'ятайте про можливість ділення на нуль і додайте перевірку цього варіанту.

# Після створення цих функцій, напишіть програму, яка імпортує модуль `calculator.py` 
# і використовує його функції для виконання обчислень. 
# Попросіть користувача ввести два числа і операцію (додавання, віднімання, множення або ділення), 
# і виведіть результат обчислення.

import calculator

write_a = int(input("Enter number a: "))
write_b = int(input("Enter number b: "))
write_option = input("Enter option add, subtract, multiply, divide: ")

def calculate(a, b, option):
    if option == 'add':
        calculator.add(a, b)
    elif option == 'subtract':
        calculator.subtract(a, b)
    elif option == 'multiply':
        calculator.multiply(a, b)
    elif option == 'divide':
        calculator.divide(a,b)
    else:
        print(f"Unfortunately your option '{option}' is not correct")
        print("You can write next option: add, subtract, multiply or divide")

calculate(write_a, write_b, write_option)