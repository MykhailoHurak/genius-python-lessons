# Списки та їхні Методи

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
b = ["Ukraine", "Sweden", "Norway", "Portugal", "Germany", "Italy", "Spain", "France", "England", "Croatia"]

print("індекс елемента 10:", a.index(10))
print("індекс елемента Ukraine:", b.index("Ukraine"))

a.append(21)
print(a)
b.append("Finland")
print(b)

a.insert(2, "Italy")
print(a)
b.insert(5, 2025)
print(b)

a.remove("Italy")
print(a)
b.remove(2025)
print(b)

last_element_a = a.pop()
print("last_element_a: ", last_element_a)
last_element_b = b.pop()
print("last_element_b: ", last_element_b)
first_element_b = b.pop(0)
print("first_element_b: ", first_element_b)
third_element_a = a.pop(2)
print("third_element_a: ", third_element_a)

a. extend([10, 10, 10])
print("кількість елементів 10: ", a.count(10))
b.extend(["Italy", "Italy"])
print("кількість елементів Italy: ", b.count("Italy"))

print(a)
print(b)

a.sort()
print(a)

b.sort()
print(b)

a.sort(reverse=True)
print(a)

a.reverse()
print(a)