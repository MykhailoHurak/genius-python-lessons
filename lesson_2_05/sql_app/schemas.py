# Файл, в яокму будемо визначати класи для Pydantic
# для того, щоб все реалізувати

from pydantic import BaseModel # цей клас використовуємо для початкого визначення методів для роботи з ашими класами

class ItemBase(BaseModel):
    title: str
    description: str | None = None

class ItemCreate(ItemBase):
    pass 

class Item(ItemBase):
    id: int
    owner_id: int

    class Config: 
        from_attributes = True # це обовязково! передає інформацію до Pydantic, що ми працюємо з ОРМ

# =======

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        from_attributes = True # це обовязково! передає інформацію до Pydantic, що ми працюємо з ОРМ