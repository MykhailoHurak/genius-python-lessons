# Цей файл потрібний для конекту з базою даних

# Команда для запуску:
# uvicorn sql_app.main:app --reload

import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("POSTGRESQL_URL")
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:1@localhost/fast_api_genius_study"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# conn = engine.connect()
# print(conn.get_isolation_level())