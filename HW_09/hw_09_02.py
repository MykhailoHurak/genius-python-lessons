# Завдання 2: Принцип відкритості/закритості (Open/Closed Principle - OCP)

# Створіть інтерфейс "Фігура" (Shape) та два класи, які реалізують цей інтерфейс, 
# наприклад, "Коло" (Circle) та "Прямокутник" (Rectangle). 
# Потім додайте новий клас, який розраховує площу будь-якої фігури, не модифікуючи існуючі класи. 
# Використовуйте принцип OCP для розширення функціональності.

from abc import ABC, abstractclassmethod

class Shape(ABC):
    """class Shape"""
    pass

class CalculateArea(ABC):
    """class CalculateArea"""

    @abstractclassmethod
    def calculate_area(self):
        pass

class Circle(Shape, CalculateArea):
    """class Circle"""
    
    def __init__(self, r):
        self.r = r

    def calculate_area(self):
        area = 3.14 * self.r ** 2
        print(f"Area of Circle (r={self.r}) = {area}")
        return area

class Rectangle(Shape, CalculateArea):
    """class Rectangle"""

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate_area(self):
        area = self.a * self.b
        print(f"Area of Rectangle (a={self.a}, b={self.b}) = {area}")
        return area
    
circle1 = Circle(6)
circle1.calculate_area()

rectangle1 = Rectangle(3, 7)
rectangle1.calculate_area()