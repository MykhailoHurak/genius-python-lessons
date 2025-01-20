# Цикли:
# Таблиця множення:
# Завдання: 
# Виведіть таблицю множення для заданого числа від 1 до 10.

# number = 5
number = int(input("Enter the number from 1 to 10: "))

a = 1

if number < 1 and number > 10:
    print("Error! You wrote wrong number")
else:
    while a <= 10:
        print(f"{number} * {a} = {number * a}")
        a += 1