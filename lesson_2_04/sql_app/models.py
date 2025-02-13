# Файл, в якому визначені моделі

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String # імпортуємо типи наших даних
from sqlalchemy.orm import relationship # фукція, яка потрібна, щоб встановити більш зрозуміле відношення між обєктами

from .database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship('Item', back_populates='owner')

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship('User', back_populates='items')