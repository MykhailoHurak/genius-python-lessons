# Цикли:
# Пошук простих чисел:
# Завдання: 
# Знайдіть всі прості числа в заданому діапазоні.

# prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19]
list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
prime_numbers = []


for number in list_numbers:
    a = number
    count = 0
    while a > 0:
        if number % a == 0:
            count += 1
        a -= 1
        # print(f"number {number},  a = {a}, count = {count}")
    if count == 2:
        print(f"Number {number} is PRIME")
        prime_numbers.append(number)
    else:
        print(f"Number {number} is not prime")

print(f"prime_numbers = {prime_numbers}")