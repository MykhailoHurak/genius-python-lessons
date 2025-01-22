# Завдання 2: Поліморфізм

# Створіть метод `display_info()` у базовому класі `Vehicle`, 
# який виводить загальну інформацію про транспортний засіб 
# (наприклад, "Це [виробник] [модель] [рік] року виробництва.").

# В кожному з підкласів перевизначте метод `display_info()` 
# для виведення специфічної інформації про цей вид транспорту.

# Створіть список об'єктів з різних видів транспорту, 
# викличте метод `display_info()` для кожного об'єкта, 
# і спостерігайте за тим, як поліморфізм дозволяє викликати правильну версію методу для кожного об'єкта.

class Vehicle:
    """class Vehicle"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"General info: This {self.model} made in {self.make} in {self.year}")

class Car(Vehicle):
    """class Car"""

    def __init__(self, make, model, year, unique_attr_car):
        super().__init__(make, model, year)
        self.unique_attr_car = unique_attr_car

    def unique_method_car(self):
        print(f"This is unique method for CAR with {self.unique_attr_car}")

    def display_info(self):
        super().display_info()
        print(f"This CAR uses {self.unique_attr_car}")

class Motorcycle(Vehicle):
    """class Motorcycle"""

    def __init__(self, make, model, year, unique_attr_motorcycle):
        super().__init__(make, model, year)
        self.unique_attr_motorcycle = unique_attr_motorcycle

    def unique_method_motorcycle(self):
        print(f"This is unique method for MOTORCYCLE with {self.unique_attr_motorcycle}")
    
    def display_info(self):
        super().display_info()
        print(f"This MOTORCYCLE uses {self.unique_attr_motorcycle}")

class Bicycle(Vehicle):
    """class Bicycle"""

    def __init__(self, make, model, year, unique_attr_bicycle):
        super().__init__(make, model, year)
        self.unique_attr_bicycle = unique_attr_bicycle

    def unique_method_bicycle(self):
        print(f"This is unique method for BICYCLE with {self.unique_attr_bicycle}")

    def display_info(self):
        super().display_info()
        print(f"This BICYCLE uses {self.unique_attr_bicycle}")

car1 = Car("Ukraine", "Model Car", 2025, "Unique attribute for Car")
car1.display_info()

motorcycle1 = Motorcycle("Norway", "Model Motorcycle", 2020, "Unique attribute for Motorcycle")
motorcycle1.display_info()

bicycle1 = Bicycle("Germany", "Model Bicycle", 2015, "Unique attribute for Bicycle")
bicycle1.display_info()