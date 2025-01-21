# Ініціалізація об'єктів через конструктор

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Mykhailo", 33)
person2 = Person("Miguel", 44)

print(person1.name)
print(person1.age)

print(person2.name)
print(person2.age)