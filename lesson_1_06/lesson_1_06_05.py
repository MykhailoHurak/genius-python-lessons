# Ініціалізація об'єктів через конструктор

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_attributes(self):
        print(f">>>>>>> {self} <<<<<<<")
        print(self.name, self.age)

person1 = Person("Michael", 25)
print(person1)
person1.print_attributes()

person2 = Person("Mykhailo", 33)
print(person2)
person2.print_attributes()
