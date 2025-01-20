# Використати вивчені функції Python:

# Робота з рядками:
#  1. Cтворити змінну num_str = 125, перевести її в тип string за допогою функції str()
#  2. Cтворити зміну message = 'Hi, my name is Python!' За допомогою функції replace() замінити  
# усі букви 'y' на '0' та 'i' на '1'.
#  3. Cтворити зміну split_test = 'This is a split test' і розділити її по пробілах за 
# допомогою функції split(), а потім знову обʼєднати у строку за допомогою функції join() у змінну string_join
#  4. Визначити довжину рядку string_join за допомогою функції len()

#  =================================================================

#  1. Cтворити змінну num_str = 125, перевести її в тип string за допогою функції str()

num_str = 125
result_1 = str(num_str)
print(type(result_1))

#  2. Cтворити зміну message = 'Hi, my name is Python!' За допомогою функції replace() замінити  

message = 'Hi, my name is Python!'
result_2 = message.replace("y", "0").replace("i", "1")
print(result_2)
print(type(message))
print(type(result_2))

#  3. Cтворити зміну split_test = 'This is a split test' і розділити її по пробілах за 
# допомогою функції split(), а потім знову обʼєднати у строку за допомогою функції join() у змінну string_join

split_test = 'This is a split test'
result_3 = split_test.split()
print(result_3)

string_join = " ".join(result_3)
print(string_join)

#  4. Визначити довжину рядку string_join за допомогою функції len()

result_4 = len(string_join)
print(result_4)