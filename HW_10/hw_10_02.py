# Завдання 2: Параметри запиту

# Розширте попереднє завдання, додаючи можливість вказати параметри запиту. 
# Виконайте GET-запит до веб-ресурсу https://jsonplaceholder.typicode.com, 
# передаючи параметри запиту, такі як параметри запиту у URL або параметри через словник.

import requests

site = 'https://jsonplaceholder.typicode.com/'
site_posts = 'https://jsonplaceholder.typicode.com/posts/'

param = input("Enter number from 1 to 100: ")

get_request = requests.get(site_posts + param)

if get_request.status_code == 200:
    print(get_request.text)
else:
    print(f"Error! Status code {get_request.status_code}")
