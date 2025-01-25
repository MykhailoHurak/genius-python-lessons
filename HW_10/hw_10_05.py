# Завдання 5: Обробка помилок

# Додайте обробку помилок до вашого коду. 
# Обробляйте можливі винятки, такі як requests.exceptions.RequestException, 
# та виводьте відповідні повідомлення про помилку.

import requests

# URL веб-ресурсу
site_posts = 'https://jsonplaceholder.typicode.com/posts'

try:
    get_request = requests.get(site_posts)
    get_request.raise_for_status()  # Піднімає виняток для помилок HTTP

    print('🔵 Заголовки відповіді:')
    for key, value in get_request.headers.items():
        print(f'{key}: 📍 {value}')

except requests.exceptions.RequestException as error_text:
    print(f'🔴 Виникла помилка запиту: {error_text}')