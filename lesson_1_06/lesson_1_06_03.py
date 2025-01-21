class Person: # це клас Person
    """Class for creation persons"""
    name = "Michael"
    age = 33
    height = 190

person1 = Person() # це екземпляр класу Person

# отримання значення атрибуту існуючого або перестаховна, якщо не існує
print(getattr(Person, 'name'))
print(getattr(person1, 'name'))
print(getattr(person1, 'counrty', 'counrty attribute not found'))

# додавання нового атрибуту або зміна існуючого
setattr(person1, 'age', 25)
setattr(person1, 'height', 185)
print(person1.age)
print(person1.height)
print(person1.__dict__)

# перевірка, чи є власні атрибути
print(hasattr(person1, 'name'))
print(hasattr(person1, 'weight'))

# видалення атрибутів (варіант 1)
del Person.height
print(Person.__dict__)
print(hasattr(Person, 'height'))

# видалення атрибутів (варіант 2)
delattr(Person, 'age')
print(Person.__dict__)
print(hasattr(Person, 'age'))

# перед видаленням атрибуту потрібно переконатись, що він існує
# виникне помилка, якщо будемо намагтись видалити неіснуючий атрибут

print(Person.__doc__) # отримання опису класу