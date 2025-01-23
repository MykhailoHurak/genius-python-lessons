# Абстракція, абстрактні класи

from abc import ABC, abstractclassmethod

class Shape(ABC):
    """class Shape"""

    @abstractclassmethod
    def area(self):
        pass

class Circle(Shape):
    """class Circle"""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = 3.14 * self.radius ** 2
        print(f"Area = {area}")
        return area
    
class Rectangle(Shape):
    """class Rectangle"""

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area = self.length * self.width
        print(f"Area = {area}")
        return area
    
circle1 = Circle(7)
circle1.area()

rectangle1 = Rectangle(3, 8)
rectangle1.area()