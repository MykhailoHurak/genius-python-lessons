# Використати вивчені оператори та порівняти між собою числа, рядки, булеві значення, списки, словники і кортежі

num_1 = 1
num_2 = 5
num_3 = 5
num_4 = 11
num_5 = 21

string_1 = "My favourite name is Mike"
string_2 = "His name is Michael"
string_3 = "Mykhailo"
string_4 = "Miguel"
string_5 = "My name is Mykhailo"

bool_1 = True
bool_2 = True
bool_3 = False
bool_4 = True
bool_5 = False

list_1 = ["HTML+CSS", "JavaScript", "Python"]
list_2 = ["React", "Angular", "Vue"]
list_3 = ["HTML+CSS"]
list_4 = ["HTML+CSS", "JavaScript", "Python"]
list_5 = ["Python"]

dictionary_1 = {"name": "Mykhailo", "age": 33, "weight": 100}
dictionary_2 = {"name": "Mike", "age": 18, "weight": 85}
dictionary_3 = {"name": "Michael", "age": 24, "weight": 90}
dictionary_4 = {"name": "Mykhailo", "age": 33, "weight": 100}
dictionary_5 = {"name": "Miguel", "age": 21, "weight": 88}

tuple_1 = (1, 2, 3, 4, 5)
tuple_2 = (1, 2, 3)
tuple_3 = ("Dynamo Kyiv", "Shakhtar Donetsk", "Chelsea London", "Real Madrid")
tuple_4 = (1, 2, 3, 4, 5)
tuple_5 = ("Dynamo Kyiv")

result_1 = num_1 > num_2
print("result_1:", result_1)
result_2 = num_2 + num_4 == num_1 * 2
print("result_2:", result_2)
result_3 = num_1 + num_2 + num_3 == num_4 and num_5 >= num_4
print("result_3:", result_3)
result_4 = num_1 * 10 == num_4 - 1 and num_5 / 7 == num_2 - 2
print("result_4:", result_4)
result_5 = num_1 == num_5 or num_3 == num_4
print("result_5:", result_5)

result_6 = "Mykhailo" in string_3
print("result_6:", result_6)
result_7 = "M" in string_1 or "G" in string_2
print("result_7:", result_7)
result_8 = string_4 != string_5 and num_2 == num_3 or num_5 < num_1
print("result_8:", result_8)
result_9 = bool_1 == False or bool_2 != False and num_1 <= num_4 and "M" in string_3
print("result_9:", result_9)
result_10 = ["HTML+CSS"] in list_1 and list_4 == list_1 or list_3 in list_1
print("result_10:", result_10)

result_11 = list_3.append(["JavaScript", "Python"]) == list_1
print("result_11:", result_11)
result_12 = dictionary_1 == dictionary_4 or dictionary_2 == dictionary_5
print("result_12:", result_12)
result_13 = tuple_5 in tuple_3
print("result_13:", result_13)
result_14 = dictionary_1.get("name") == dictionary_4.get("name") and dictionary_2["weight"] < dictionary_4["weight"]
print("result_14:", result_14)
result_15 = num_1 < num_2 and string_3 in string_5 or bool_3 == True and list_4 != list_5
print("result_15:", result_15)