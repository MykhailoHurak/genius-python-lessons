# Абстракція, абстрактні класи

from abc import ABC, abstractclassmethod

class Car(ABC):
    """class Car"""

    def __init__(self, mark, cost):
        self.mark = mark
        self.cost = cost

    @abstractclassmethod
    def car_info(self):
        pass

class Toyota(Car):
    """class Toyota"""

    def car_info(self):
        print(f"Car {self.mark} costs {self.cost}")

class Mercedes(Car):
    """class Mercedes"""

    def car_info(self):
        print(f"Car {self.mark} costs {self.cost}")

toyota1 = Toyota("Camry", 11000)
mercedes1 = Mercedes("E-Class", 22000)

toyota1.car_info()
mercedes1.car_info()

