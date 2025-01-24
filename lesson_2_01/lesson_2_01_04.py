# Урок 1: Основи веб-розробки та архітектура клієнт-сервер.

# Бібліотеку requests встановив за допомогою команди pip install requests
import requests

# PATCH - видалення і заміна тільки конкретного поля, всі інші дані зберігаєються

site_for_patch = "https://jsonplaceholder.typicode.com/posts/1"

data_test_for_patch = {
    "title": "Title for testing PATCH request"
}

print(f"Text of posts/1 before using PATCH: {requests.get(url=site_for_patch).text}")

response_for_patch = requests.patch(url=site_for_patch, data=data_test_for_patch)

print(f"🔵 PATCH Status code: {response_for_patch.status_code}")
print(f"🔵 PATCH Reason:: {response_for_patch.reason}")
print(f"🔵 PATCH Text of posts/1 after using PATCH: {response_for_patch.text}")