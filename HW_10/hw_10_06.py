# Завдання 6: Збереження вмісту в файл

# Розширте ваш код, щоб зберегти отриманий вміст веб-сторінки у файл. 
# Використайте функціонал Python для роботи з файлами для збереження вмісту.

import requests

# URL веб-ресурсу
site = 'https://jsonplaceholder.typicode.com/posts'

try:
    get_request = requests.get(site)
    get_request.raise_for_status()  # Піднімає виняток для помилок HTTP

    # Збереження вмісту веб-сторінки у файл
    with open('hw_10_06_saved_content.txt', 'w', encoding='utf-8') as file:
        file.write(get_request.text)
    
    print('Вміст веб-сторінки успішно збережено у файл hw_10_06_saved_content.txt')

except requests.exceptions.RequestException as error_text:
    print(f'Виникла помилка запиту: {error_text}')