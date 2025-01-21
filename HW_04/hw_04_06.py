# Словники:
# Робота із словниками:

# Завдання: 
# Створіть словник, що містить інформацію про вашого улюбленого спортсмена (ім'я, вік, спорт, команда тощо). 
# Виведіть цю інформацію на екран.

player = {
    'name': 'Cristiano Ronaldo',
    'age': 39,
    'sport': 'football',
    'country': 'Portugal',
}

print(player)

print("name:", player['name'])
print("age:", player['age'])
print("sport:", player['sport'])
print("country:", player['country'])

print(player.keys())
print(player.values())

print(player.items())