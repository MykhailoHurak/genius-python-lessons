# Урок 1: Основи веб-розробки та архітектура клієнт-сервер.

# Бібліотеку requests встановив за допомогою команди pip install requests
import requests

# DELETE - видалення даних 

site_for_delete = "https://jsonplaceholder.typicode.com/posts/1"

response_for_delete = requests.delete(url=site_for_delete)

print(f"🔵 DELETE Status code: {response_for_delete.status_code}")
print(f"🔵 DELETE Reason:: {response_for_delete.reason}")
print(f"🔵 DELETE Text of posts/1 after using DELETE: {response_for_delete.text}")

