# Завдання 1: Наслідування

# Створіть базовий клас `Vehicle` (транспортний засіб), який містить наступні атрибути:

# - `make` (виробник)
# - `model` (модель)
# - `year` (рік виробництва)

# Додайте конструктор класу `Vehicle`, який ініціалізує ці атрибути.

# Створіть підкласи (похідні класи) від `Vehicle` для різних видів транспорту, 
# наприклад, `Car`, `Motorcycle`, `Bicycle`, тощо. 
# Кожен підклас повинен мати додаткові атрибути та методи, 
# які є специфічними для цього виду транспорту. 
# Наприклад, для класу `Car` можна додати атрибут `fuel_type` та метод `start_engine()`.

# Створіть об'єкти для кожного з підкласів та виведіть їхні атрибути на екран.

class Vehicle:
    """class Vehicle"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Car(Vehicle):
    """class Car"""

    def __init__(self, make, model, year, unique_attr_car):
        super().__init__(make, model, year)
        self.unique_attr_car = unique_attr_car

    def unique_method_car(self):
        print(f"This is unique method for CAR with {self.unique_attr_car}")

class Motorcycle(Vehicle):
    """class Motorcycle"""

    def __init__(self, make, model, year, unique_attr_motorcycle):
        super().__init__(make, model, year)
        self.unique_attr_motorcycle = unique_attr_motorcycle

    def unique_method_motorcycle(self):
        print(f"This is unique method for MOTORCYCLE with {self.unique_attr_motorcycle}")

class Bicycle(Vehicle):
    """class Bicycle"""

    def __init__(self, make, model, year, unique_attr_bicycle):
        super().__init__(make, model, year)
        self.unique_attr_bicycle = unique_attr_bicycle

    def unique_method_bicycle(self):
        print(f"This is unique method for BICYCLE with {self.unique_attr_bicycle}")

car1 = Car("Made in Ukraine", "Model Car", 2025, "Unique attribute for Car")
car1.unique_method_car()

motorcycle1 = Motorcycle("Made in Norway", "Model Motorcycle", 2020, "Unique attribute for Motorcycle")
motorcycle1.unique_method_motorcycle()

bicycle1 = Bicycle("Made in Germany", "Model Bicycle", 2015, "Unique attribute for Bicycle")
bicycle1.unique_method_bicycle()