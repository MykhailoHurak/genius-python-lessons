# if, elif, else

user_1 = {
    "name": "Mykhailo",
    "age": 33,
    "balance": 11000,
    "status": True
}

user_2 = {
    "name": "Mike",
    "age": 17,
    "balance": 500,
    "status": True
}

user_3 = {
    "name": "Michael",
    "age": 25,
    "balance": 22000,
    "status": False
}

if user_3.get("name", None) and user_3.get("age") >= 18 and user_3["status"] == True:
    print(f"Hello, {user_3["name"]}")
elif not user_3.get("name", None):
    print(f"Hello! Please, write your name...")
elif user_3.get("age") < 18:
    print(f"Unfortunately you cannot registry due to your age")
elif user_3["status"] != True:
    print("Your status is False")
else:
    print("Something wrong")
