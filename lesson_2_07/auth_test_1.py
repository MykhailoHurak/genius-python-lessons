# Security - First Steps
# https://fastapi.tiangolo.com/tutorial/security/first-steps/

# pip install python-multipart

# uvicorn auth:app --reload
# http://127.0.0.1:8000/docs#/

# from typing import Annotated

# from fastapi import Depends, FastAPI
# from fastapi.security import OAuth2PasswordBearer

# app = FastAPI()

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# @app.get("/items/")
# async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
#     return {"token": token}