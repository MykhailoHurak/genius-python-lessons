# Цикли:
# Факторіал числа:
# Завдання: 
# Обчисліть факторіал заданого числа.

number = 3
a = number
factorial = 1

while a > 0:
    factorial *= a
    a -= 1

print(f"Factorial of number {number} is {factorial}") 