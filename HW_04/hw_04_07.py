# Словники:
# Оновлення словника:

# Завдання: 
# Створіть словник, що містить ваші улюблені книги (назва книги та рік видання). 
# Додайте до словника нову улюблену книгу та виведіть оновлений словник.

# Варіант 1 - створення словнику згідно завдання

list_books = {
    'Atomic Habits': 2018,
    'The Concise 48 Laws of Power': 2002,
    'Getting Things Done': 2019
}

list_books['Think and Grow Rich'] = 2004

print(list_books)

# Варінт 2 - створення списку словників (для практики)

books = [
    {'title': 'Atomic Habits', 'author': 'James Clear', 'year': 2018},
    {'title': 'The Concise 48 Laws of Power', 'author': 'Robert Greene', 'year': 2002},
    {'title': 'Getting Things Done', 'author': 'David Allen', 'year': 2019}
]

new_book = {'title': 'Think and Grow Rich', 'author': 'Napoleon Hill', 'year': 2004}

books.append(new_book)

print(books)

