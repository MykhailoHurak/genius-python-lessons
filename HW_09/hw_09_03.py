# Завдання 3: Принцип підстановки Лісков (Liskov Substitution Principle - LSP)

# Створіть ієрархію класів для геометричних фігур, 
# де кожен підклас (наприклад, "Квадрат" і "Круг") може замінити базовий клас "Фігура" без порушення функціональності. 
# Переконайтеся, що ці підкласи можуть використовуватися замість базового класу у всіх контекстах без проблем.

class Shape:
    """class Shape"""

    def __init__(self):
        pass

    def calculate_area(self):
        pass

class Circle(Shape):
    """clas Circle"""

    def __init__(self, r):
        super().__init__()
        self.r = r

    def calculate_area(self):
        area = 3.14 * self.r ** 2
        print(f"Area of Circle (r={self.r}) is {area}")
        return area

class Rectangle(Shape):
    """class Rectangle"""

    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b
    
    def calculate_area(self):
        area = self.a * self.b
        print(f"Area of Rectangle (a={self.a}, b={self.b}) is {area}")
        return area
    
circle1 = Circle(3)
circle1.calculate_area()

rectangle1 = Rectangle(3, 5)
rectangle1.calculate_area()