# Завдання 1: Створення класу і об'єктів

# Створіть клас `Animal`, який представляє тварину. 
# Кожний об'єкт класу `Animal` повинен мати наступні атрибути:

# - `name` (ім'я тварини)
# - `species` (вид тварини)
# - `age` (вік тварини)

# Створіть конструктор класу, який ініціалізує ці атрибути при створенні об'єкта. 
# Напишіть метод `make_sound()`, який буде виводити звук, який виділяє тварина.

# Створіть два об'єкта класу `Animal` з різними характеристиками та викличте їхні методи `make_sound()`.

class Animal:
    """Class for presentation of animals"""

    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def make_sound(self, sound):
        print(f"{self.species} {self.name} says {sound}")

animal1 = Animal('Rock', 'dog', 5)
animal2 = Animal('Tom', 'cat', 2)

animal1.make_sound('Hav-Hav-Hav')
animal2.make_sound('Miau-Miau-Miau')