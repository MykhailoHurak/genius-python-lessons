# Оператори

# Додавання
num_1 = 100
num_2 = 10
result = num_1 + num_2
print(result)

# Віднімання
num_1 = 100
num_2 = 10
result = num_1 - num_2
print(result)

# Множення
num_1 = 100
num_2 = 10
result = num_1 * num_2
print(result)

# Ділення
num_1 = 100
num_2 = 10
result = num_1 / num_2
print(result)

# Ділення звичайне та цілочисельне
num_1 = 7
num_2 = 2

num_3 = num_1 / num_2
num_4 = num_1 // num_2

print(num_3)
print(num_4)

# Возведення числа у ступінь
num_1 = 5
num_2 = 2

num_3 = num_1 ** num_2
print(num_3)

# Залишок від ділення
num_1 = 7
num_2 = 2

num_3 = num_1 % num_2
print(num_3)

# Оператори порівняння == Дорівнює
num_1 = 7
num_2 = 2

num_3 = num_1 == num_2
print(num_3)

# Оператори порівняння != Не дорівнює
num_1 = 7
num_2 = 2

num_3 = num_1 != num_2
print(num_3)

# Оператори порівняння < Менше
num_1 = 7
num_2 = 2

num_3 = num_1 < num_2
print(num_3)

# Оператори порівняння > Більше
num_1 = 7
num_2 = 2

num_3 = num_1 > num_2
print(num_3)

# Оператор Логічний and
num = 10
name = "Mike"

result = num > 5 and name == "Mike"
print(result)

# Оператор Логічний or
num = 10
name = "Mike"

result = num < 5 or name == "Mike"
print(result)

# Оператор Логічний in, not in
num = 10
name = "Mike"
message_1 = "Mike got some money"
message_2 = "You won"

print(name in message_1)
print(name not in message_1)

print(name in message_2)
print(name not in message_2)