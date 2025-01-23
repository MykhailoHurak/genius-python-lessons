# Абстракція, абстрактні класи

from abc import ABC, abstractclassmethod

class Animal(ABC):
    @abstractclassmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Hav-Hav-Hav!"
    
class Cat(Animal):
    def speak(self):
        return "Miau-Miau-Miau!"
    
# Не можна створити екземпляр абстрактного класу Animal
# animal = Animal() # отримаємо помилку