# Умовні конструкції:
# Визначення днів тижня:
# Завдання: 
# Створіть програму, яка встановлює номер дня тижня і виводить назву відповідного дня тижня. 
# Якщо номер дня недійсний (менше 1 або більше 7), виведіть повідомлення про помилку.

# day_number = 5
# day_number = int(input())
day_number = int(input("Введіть номер дня тижня (1-7): "))

if day_number < 1 and day_number > 7:
    print("Error! Please, write correct number from 1 to 7")
else:
    if day_number == 1:
        print(f"{day_number}: Today is Monday")
    elif day_number == 2:
        print(f"{day_number}: Today is Tuesday")
    elif day_number == 3:
        print(f"{day_number}: Today is Wednesday")
    elif day_number == 4:
        print(f"{day_number}: Today is Thursday")
    elif day_number == 5:
        print(f"{day_number}: Today is Friday")
    elif day_number == 6:
        print(f"{day_number}: Today is Saturday")
    elif day_number == 7:
        print(f"{day_number}: Today is Sunday")