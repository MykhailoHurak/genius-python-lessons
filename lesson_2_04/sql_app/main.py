# Файл, звідки у нас буде іти запуск і створення самого обєкта sql_app

from fastapi import FastAPI

from . import models
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Hello World'}