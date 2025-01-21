# Словники

user = {
    "name": "Mike",
    "age": 33,
    "country": "Ukraine"
}

print("user['name']:", user['name'])
print("user['age']:", user['age'])
print("user['country']:", user['country'])

# print(user["height"]) - помилка, якщо так звернутись до неіснуючого ключа
print('user.get("height", "Key not found"):', user.get("height", "Key not found"))

user['name'] = "Mykhailo" # змінюємо значення ключа
user['age'] = 22 # змінюємо значення ключа

user['height'] = 185 # додаємо ключ-значення
user["weight"] = 85 # додаємо ключ-значення
print("user['weight']:", user["weight"])
print(user)

