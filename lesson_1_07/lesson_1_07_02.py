# Поліморфізм через успадкування
# Поліморфізм - здатність обєктів різних класів виконувати однакові методи
# Успадковані методи можуть бути перевизначені у підкласах

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length
        
    def area(self):
        return self.side_length ** 2
    
circle1 = Circle(10)
square1 = Square(7)

print("Circle area = ", circle1.area())
print("Square area = ", square1.area())