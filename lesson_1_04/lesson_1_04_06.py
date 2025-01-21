# Словники та їхні Методи

user = {
    "name": "Mike",
    "age": 33,
    "country": "Ukraine"
}

user_copy = user.copy() # створили копію словника

print(user, "- user") # оригвнальний словник
print(user_copy, "- user_copy") # копія словника 

user_copy.clear() # очистили копію словника, тепер він пустий
print(user_copy, "- user_copy")

for item in user:
    print(item)

for key, value in user.items():
    print(f"{key}: {value}")

for a, b in user.items():
    print(f"{a}: {b}")

key_weight = user.pop("weight", "Cannot delete because key not found")
print(key_weight)

user_new_elements = {"city": "Kyiv", "height": 185, "weight": 85} # створюємо словник
user_update = user.update(user_new_elements) # розширюємо наш словник
print(user)