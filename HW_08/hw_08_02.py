# Завдання 2: Абстракція

# Створіть клас "Фігура" (Shape), який буде абстрактним класом. 
# У цьому класі визначіть абстрактний метод "обчислити_площу" (calculate_area).

# Створіть підкласи цього класу для різних геометричних фігур, наприклад, 
# "Коло" (Circle), "Прямокутник" (Rectangle) і "Трикутник" (Triangle). 
# У кожному з підкласів реалізуйте метод "обчислити_площу" відповідно до формули для обчислення площі кожної фігури.

# Створіть об'єкти кожного з підкласів і використайте метод "обчислити_площу", щоб вивести площу кожної фігури на екран.

from abc import ABC, abstractclassmethod

class Shape(ABC):
    """class Shape"""

    @abstractclassmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    """class Circle"""

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        area = 3.14 * self.radius ** 2
        print(f"Area of circle (r={self.radius}) = {area}")
        return area
    
class Rectangle(Shape):
    """class Rectangle"""

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate_area(self):
        area = self.a * self.b
        print(f"Area of rectangle (a={self.a}, b={self.b}) = {area}")
        return area

class Triangle(Shape):
    """class Triangle"""

    def __init__(self, a, h):
        self.a = a
        self.h = h

    def calculate_area(self):
        area = self.a * self.h / 2
        print(f"Area of triangle (a={self.a}, h={self.h}) = {area}")
        return area

circle1 = Circle(5)
circle1.calculate_area()

rectangle1 = Rectangle(4, 6)
rectangle1.calculate_area()

triangle1 = Triangle(10, 4)
triangle1.calculate_area()