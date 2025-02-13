# Урок 2: Введення до FastAPI. Встановлення та перша програма.
# https://fastapi.tiangolo.com/

# First Steps - Install
# https://fastapi.tiangolo.com/tutorial/first-steps/

# Запуск сервера
# ...\lesson_2_02> fastapi dev lesson_2_02_02.py - команда для запуску сервера

# Path Parameters
# https://fastapi.tiangolo.com/tutorial/path-params/

# http://127.0.0.1:8000/docs#/

from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}
