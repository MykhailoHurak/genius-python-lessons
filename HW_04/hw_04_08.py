# Словники:
# Пошук значення:

# Завдання: 
# Створіть словник, що містить інформацію про країни та їх столиці. 
# Запитайте користувача про назву країни і виведіть столицю цієї країни (якщо така країна є у словнику).

globus = {
    'Ukraine': 'Kyiv',
    'England': 'London',
    'Spain': 'Madrid',
    'Italy': 'Rome',
    'Germany': 'Berlin',
    'France': 'Paris',
    'Portugal': 'Lissbon'
}

check_country = input("Enter the country name: ")

if check_country in globus:
    print(f"The capital of {check_country} is {globus[check_country]}")
else:
    print(f"Sorry, we don't have an information about country {check_country}")