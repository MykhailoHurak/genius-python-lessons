# Урок 1: Основи веб-розробки та архітектура клієнт-сервер.

# Бібліотеку requests встановив за допомогою команди pip install requests
import requests

# POST - створення нових даних

site_for_post = "https://jsonplaceholder.typicode.com/posts"

body_for_post = {
    'userId': 12345, 
    'title': 'Test Title for POST', 
    'body': 'Test Body for POST'
}

headers_for_post = {
    'Content-Type': 'application/json; charset=utf-8'
}

response_for_post = requests.post(url=site_for_post, json=body_for_post, headers=headers_for_post)

print(f"🔵 POST Status code: {response_for_post.status_code}")
print(f"🔵 POST Reason:: {response_for_post.reason}")
print(f"🔵 POST Text of posts/1 after using POST: {response_for_post.text}")