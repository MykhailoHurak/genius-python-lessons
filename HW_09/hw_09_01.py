# Завдання 1: Принцип єдиного обов'язку (Single Responsibility Principle - SRP)

# Спроектуйте і реалізуйте клас "Користувач" (User), який відповідає принципу SRP. 
# В цьому класі повинні бути методи для створення користувача, оновлення даних користувача та видалення користувача. 
# Переконайтеся, що кожен метод відповідає за одну конкретну функцію.

class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

class UserManager:
    def create_user(self, user_id, name, email):
        return User(user_id, name, email)
    
    def update_user(self, user, name=None, email=None):
        if name:
            user.name = name
        if email:
            user.email = email
    
    def delete_user(self, user):
        del user

# Приклад використання
user_manager = UserManager()

# Створення користувача
new_user = user_manager.create_user(1, "Іван", "ivan@example.com")

# Оновлення даних користувача
user_manager.update_user(new_user, email="ivan_new@example.com")

# Видалення користувача
user_manager.delete_user(new_user)
