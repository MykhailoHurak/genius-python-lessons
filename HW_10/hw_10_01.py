# Завдання 1: Виконання GET-запиту

# Створіть Python-сценарій, який використовує бібліотеку requests 
# для виконання GET-запиту до веб-ресурсу https://jsonplaceholder.typicode.com
# та виведення вмісту веб-сторінки на екран. 
# Використовуйте функцію requests.get() для виконання запиту.

import requests

site = "https://jsonplaceholder.typicode.com/"

get_request = requests.get(site + 'postsw')

print(get_request.text)

# =================================================

if get_request.status_code == 200:
    print(get_request.text)
else:
    print(f"Error! Status code {get_request.status_code}")