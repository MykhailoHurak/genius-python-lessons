# Вбудовані функції для роботи з типами даних

# Функції для чисел

num_1 = '111'
print("num_1 =", num_1)
print("Тип числа num_1:", type(num_1))

num_2 = int(num_1)
print("num_2 =", num_2)
print("Тип числа num_2:", type(num_2))

num_3 = float(num_1)
print("num_3 =", num_3)
print("Тип числа num_3:", type(num_3))

# Функції для рядків

string_1 = 'hello world!'
print("Кількість символів у рядку string_1:", len(string_1))

string_2 = string_1.upper()
print(string_2)

string_3 = string_2.lower()
print(string_3)

string_4 = string_3.capitalize()
print(string_4)

string_5 = string_4.replace("!", ".")
print(string_5)

string_6 = string_5.split()
print(string_6)

string_7 = " ".join(string_6)
print(string_7)

string_8 = string_7.count("o")
print(string_8)

string_9 = 111
print(type(string_9))
string_10 = str(string_9)
print(type(string_10))

# Функції для списків та кортежів

my_list_1 = [1, 2, 3]
print(len(my_list_1))
print(my_list_1)

my_list_2 = my_list_1
my_list_2.append(4)
print(my_list_2)

my_list_3 = my_list_2
my_list_3.extend([5, 6, 7])
print(my_list_3)

print(my_list_3.index(5))

# Функції для словників

my_dictionary = {"name": "Michael", "age": 33, "high": 185}
print(my_dictionary.keys())
print(my_dictionary.values())
print(my_dictionary.items())

print("Name:", my_dictionary["name"])
print("Name:", my_dictionary.get("name"))
print("Weigh:", my_dictionary.get("weight", "---"))