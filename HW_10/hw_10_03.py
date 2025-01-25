# Завдання 3: POST-запит

# Створіть Python-сценарій для виконання POST-запиту до веб-ресурсу https://jsonplaceholder.typicode.com. 
# Відправте дані на сервер, наприклад, форму з ім'ям користувача і паролем.

import requests

site = 'https://jsonplaceholder.typicode.com/posts'

data_1_to_post = {
    "name": "Mykhailo",
    "email": "mykhailo@email.com",
    "password": "qwerty12345"
}

post_request = requests.post(site, json=data_1_to_post)

if post_request.status_code == 201:
    print(f"Status code: {post_request.status_code}")
    print(post_request.json())
else:
    print(f"Error! Status code: {post_request.status_code}")
