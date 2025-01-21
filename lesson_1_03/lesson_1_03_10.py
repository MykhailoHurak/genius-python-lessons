# for
# while
# if, elif, else
# continue

user_1 = {
    "name": "Mike",
    "role": "Junior",
    "status": True
}

user_2 = {
    "name": "Mykhailo",
    "role": "Senior",
    "status": False
}

user_3 = {
    "name": "Myshko",
    "role": "BOSS",
    "status": True
}

user_4 = {
    "name": "Michael",
    "role": "Middle",
    "status": True
}

list_users = [user_1, user_2, user_3]

for user in list_users:
    print(f"Let's Go {user.get("name")}")
    if not user["status"]:
        count_of_tries = 10
        while count_of_tries > 0:
            print(f"try to connect to user {user["name"]}")
            count_of_tries = count_of_tries - 1
            if count_of_tries == 5:
                print("middle")
                continue
            print(f"{count_of_tries} attempts left")
    elif user.get("name") == "BOSS":
        print(f"Hello BIG {"role"} {"name"}")
    else:
        print(f"Ho-ho-ho {user["name"]}")
