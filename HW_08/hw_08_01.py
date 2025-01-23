# Завдання 1: Інкапсуляція

# Створіть клас "Користувач" (User), який має такі приватні поля (інкапсульовані дані):

# Ім'я (name)
# Електронна пошта (email)
# Пароль (password)

# Напишіть публічні методи для установки і отримання значень цих полів (геттери і сеттери). 
# Потім створіть об'єкт класу "Користувач" і встановіть значення полів, а також виведіть їх на екран.

class User:
    """class User"""

    def __init__(self, name, email, password):
        self._name = name
        self._email = email
        self._password = password

    def get_data(self):
        print(self.__dict__)

    def set_name(self, name):
        self._name = name
        print(f"Updated name is {self._name}")

    def set_email(self, email):
        self._email = email
        print(f"Updated email is {self._email}")

    def set_password(self, password):
        self._password = password
        print(f"Updated password is {self._password}")

user1 = User('Mykhailo', 'mykhailo@gmail.com', 'qwerty123')
user1.get_data()

user1.set_name('Michael')
user1.set_email('Michael@gmail.com')
user1.set_password('abc456')

user1.get_data()