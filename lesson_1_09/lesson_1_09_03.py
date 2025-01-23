# Урок 9: Принципи SOLID в ООП.
# ➢ Принцип підстановки Барбари Лісков (Liskov Substitution Principle). 
# Обєкт базового класу має бути замінений обєктом підкласу без порушення роботи програми

class Car:
    """class Car"""

    def __init__(self, type):
        self.type = type
        self.properties = {}

    def set_properties(self, color, cost):
        self.properties = {"Color": color, "Cost": cost}

class Car1(Car):
    """class Car1"""

    def __init__(self, type):
        super().__init__(type)

car = Car("Toyota")
car.set_properties("Black", 11000)

car1 = Car1("Volvo")
car1.properties = {"Color": "White", "Cost": 22000}

car2 = Car1("Volvo")
car2.set_properties("Black", 33000)

print(car.properties)
print(car1.properties)
print(car2.properties)


list_cars = [car, car1, car2]

def get_concret_color_car(color):
    count = 0
    for c in list_cars:
        if color == c.properties["Color"]:
            count += 1
    print(f"We have {count} {color} Car(s)")

get_concret_color_car("Black")