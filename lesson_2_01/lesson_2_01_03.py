# Урок 1: Основи веб-розробки та архітектура клієнт-сервер.

# Бібліотеку requests встановив за допомогою команди pip install requests
import requests

# PUT - видалення і заміна новими данними

site_for_put = "https://jsonplaceholder.typicode.com/posts/1"

data_test_for_put = {
    "title": "Title for testing PUT request"
}

print(f"Text of posts/1 before using PUT: {requests.get(url=site_for_put).text}")

response_for_put = requests.put(url=site_for_put, data=data_test_for_put)

print(f"🔵 PUT Status code: {response_for_put.status_code}")
print(f"🔵 PUT Reason:: {response_for_put.reason}")
print(f"🔵 PUT Text of posts/1 after using PUT: {response_for_put.text}")