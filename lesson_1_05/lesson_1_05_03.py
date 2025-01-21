def say_hello(username):
    print(f"Hello, {username}!")
    print("-------")

say_hello("Mike")

# ===================================================

def hello_name_age(name, age):
    print(f"Hello, {name}!")
    print(f"Your age is {age}. You are so beautiful!")
    print("-------")

users = {
    "Mike": 22,
    "Mykhailo": 33,
    "Michael": 11
}

for name, age in users.items():
    hello_name_age(name, age)