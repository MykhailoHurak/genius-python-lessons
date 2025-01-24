# Урок 1: Основи веб-розробки та архітектура клієнт-сервер.

# Бібліотеку requests встановив за допомогою команди pip install requests
import requests

# GET - отримання даних

site_for_get = "https://jsonplaceholder.typicode.com/"

response_for_get = requests.get(url=site_for_get)

print(f"🔵 GET Status code: {response_for_get.status_code}")
print(response_for_get) 
print(F"🔵 GET We got HTML: {response_for_get.text}") 