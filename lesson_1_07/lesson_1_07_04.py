class Vehicle:
    """Base class Vahicle"""

    def __init__(self, type, color, condition=100):
        self.type = type
        self.color = color
        self.condition = condition

    def move(self):
        print("def move() is running: Your vehicle is moving")

    def fix(self):
        if self.condition <= 50:
            print(f"You need to fix your {self.color} {self.type}")
        else:
            print(f"Your {self.color} {self.type} is in good condition. It doesn't need to fix")

class Car(Vehicle):
    """Class Car"""

    def __init__(self, type, color, condition, cost=0):
        super().__init__(type, color, condition)
        self.cost = cost
    
    def run_endine(self):
        super().move() # викликали унаслідуваний метод у батьківського класу локально
        print("Run engine")

    def move(self):
        print(f"Your {self.color} {self.type} is driving")
        print(f"Your {self.color} {self.type} costs {self.cost} dollars")

class Bicycle(Vehicle):
    """Class Bicycle"""

    def __init__(self, type, color, condition, count_of_wheels):
        super().__init__(type, color, condition)
        self.count_of_wheels = count_of_wheels

    def run_bicycle(self):
        print("Your bicycle is moving")

car1 = Car("BMW", "black", 70, 11000)
car1.run_endine()
car1.move()
car1.fix()

bicycle1 = Bicycle("Road Bike", "red", 45, 2000)
bicycle1.move()
bicycle1.fix()