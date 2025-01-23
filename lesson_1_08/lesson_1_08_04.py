# Абстракція, абстрактні класи

from abc import ABC, abstractclassmethod

class Animal(ABC):
    """class Animal"""

    @abstractclassmethod
    def move(self):
        pass

    @abstractclassmethod
    def eat(self):
        pass

class Dog(Animal):
    """class Dog"""

    def __init__(self, color, age):
        self.color = color
        self.age = age

    def move(self):
        print(f"{self.color} dog fast runs")

    def eat(self):
        print(f"Dog is {self.age} years old. Dog eats meat")

class Cat(Animal):
    """class Cat"""

    def __init__(self, distance, food):
        self.distance = distance
        self.food = food

    def move(self):
        print(f"Today cat runs {self.distance} m")

    def eat(self):
        print(f"Today cat ate {self.food}")

class AnimalType(Animal):
    pass

class Bird(AnimalType):
    """class Bird"""

    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"Bird {self.name} is flying")

    def eat(self):
        print(f"Bird {self.name} eats granes")

dog1 = Dog("black", 5)
dog1.move()
dog1.eat()

cat1 = Cat(500, "fish")
cat1.move()
cat1.eat()

bird1 = Bird("John")
bird1.move()
bird1.eat()