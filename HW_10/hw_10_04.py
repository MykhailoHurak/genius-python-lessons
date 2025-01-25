# Завдання 4: Обробка відповіді

# Після виконання запиту, розпарсьте вміст HTTP-відповіді та виведіть потрібну інформацію. 
# Наприклад, виведіть заголовки відповіді або вміст сторінки.

import requests

site = 'https://jsonplaceholder.typicode.com'

get_request_1 = requests.get(site + '/posts' + '/1')

if get_request_1.status_code == 200:
    print(f"Status code: {get_request_1.status_code}")
    print(get_request_1.text)
    print(f"Title: {get_request_1.json()['title']}")
else:
    print(f"Error! Status code: {get_request_1.status_code}")

# =====================================

get_request_all = requests.get(site + '/posts')

print(get_request_all.status_code)

for key, value in get_request_all.headers.items():
    print(f"🔵 {key}: 📍 {value}")
