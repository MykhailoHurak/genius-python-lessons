# Урок 2: Введення до FastAPI. Встановлення та перша програма.
# https://fastapi.tiangolo.com/

# First Steps - Install
# https://fastapi.tiangolo.com/tutorial/first-steps/

# Запуск сервера
# ...\genius-python-lessons\lesson_2_02> fastapi dev lesson_2_02_05.py - команда для запуску сервера

# Query Parameters
# https://fastapi.tiangolo.com/tutorial/query-params/

# http://127.0.0.1:8000/docs#/

from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]