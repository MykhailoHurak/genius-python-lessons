# Завдання 2: Робота з об'єктами

# Створіть клас `Rectangle`, який представляє прямокутник. 
# Кожен об'єкт класу `Rectangle` повинен мати наступні атрибути:

# - `width` (ширина прямокутника)
# - `height` (висота прямокутника)

# Створіть конструктор класу, який ініціалізує ці атрибути при створенні об'єкта. 
# Напишіть метод `calculate_area()`, який розраховує площу прямокутника (площа = ширина * висота).

# Створіть два об'єкта класу `Rectangle` з різними розмірами та викличте їхні методи `calculate_area()`, 
# виведіть площу прямокутників на екран.

class Rectangle:
    """Class create rectangles"""

    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        area = self.width * self.height
        print(f"Area of rectangle (width:{self.width}, height:{self.height}) = {area}")

rectangle1 = Rectangle(5, 10)
rectangle2 = Rectangle(7, 11)

rectangle1.calculate_area()
rectangle2.calculate_area()