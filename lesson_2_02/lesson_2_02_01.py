# Урок 2: Введення до FastAPI. Встановлення та перша програма.
# https://fastapi.tiangolo.com/

# First Steps - Install
# https://fastapi.tiangolo.com/tutorial/first-steps/

# Запуск сервера
# ...\genius-python-lessons\lesson_2_02> fastapi dev lesson_2_02_01.py - команда для запуску сервера

# Path Parameters
# https://fastapi.tiangolo.com/tutorial/path-params/

# http://127.0.0.1:8000/docs#/

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

