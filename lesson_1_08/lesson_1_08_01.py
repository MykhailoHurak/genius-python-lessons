# Інкапсуляція

class Student:
    def __init__(self, name, age):
        self._name = name # це захищений атрибут
        self._age = age # це захищений атрибут

    # це публічний метод для ОТРИМАННЯ імені
    def get_name(self):
        return self._name
    
    # це публічний метод для ЗМІНИ імені
    def set_name(self, name):
        self._name = name

# створюємо обєкт класу Student
student1 = Student("Mykgailo", 18)

# отримуємо імя за допомогою публічного методу
print(student1.get_name()) # Mykhailo

# змінюємо імя за допомогою публічного методу
student1.set_name("Michael")
print(student1.get_name()) # Michael

# !!! змінюємо імя через прямий доступ до захищеного атрибуту (НЕ РЕКОМЕНТУЄТЬСЯ)
student1._name = "Miguel"
print(student1.get_name()) # Miguel