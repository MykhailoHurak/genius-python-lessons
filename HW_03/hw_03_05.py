# Цикли:
# Парні числа:
# Завдання: 
# Виведіть всі парні числа від 1 до 50.

even_numbers = []

number = 1
while number <= 50:
    if number % 2 == 0:
        even_numbers.append(number)
    number += 1

print(f"even_numbers: {even_numbers}")