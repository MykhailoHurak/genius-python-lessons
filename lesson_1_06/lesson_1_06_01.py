class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old"
    
person1 = Person("Mike", 22)
person2 = Person("Mykhailo", 33)

print(person1.name)
print(person1.age)
print(person1.greet())

print(person2.name)
print(person2.age)
print(person2.greet())