# Урок 2: Введення до FastAPI. Встановлення та перша програма.
# https://fastapi.tiangolo.com/

# First Steps - Install
# https://fastapi.tiangolo.com/tutorial/first-steps/

# Запуск сервера
# ...\lesson_2_02> fastapi dev lesson_2_02_04.py - команда для запуску сервера

# Path Parameters
# https://fastapi.tiangolo.com/tutorial/path-params/

# http://127.0.0.1:8000/docs#/

from enum import Enum
from fastapi import FastAPI

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}