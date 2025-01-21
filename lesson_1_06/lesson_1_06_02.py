class Person: # це клас Person
    name = "Michael"
    age = 33

print(Person.name, Person.age)

Person.name = "Mykhailo"
Person.age = 25

print(Person.name, Person.age)

print(Person.__dict__) # подивимось, що лежить в класі Person

person1 = Person() # це екземпляр класу Person
print(person1) # <__main__.Person object at 0x00000223BB5A6F90>
print(person1.__dict__) # {}
person1.height = 185
print(person1.__dict__) # {'height': 185} - є власний атрибут, який додали раніше