from fastapi import FastAPI, Depends, HTTPException
from starception import StarceptionMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.wsgi import WSGIMiddleware
from django.core.wsgi import get_wsgi_application
import os
import django
from datetime import timedelta, time

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from fastapi.staticfiles import StaticFiles
from store.endpoints import router as store_router
from pydantic import BaseModel, EmailStr
from typing import Optional
from utils import authenticate_user, create_access_token, create_refresh_token, register_user 

django_app = get_wsgi_application()

app = FastAPI(debug=True) 

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

app.mount('/django/static', StaticFiles(directory='static'), name='static')
# mount images
app.mount('/django/images', StaticFiles(directory='images'), name='media')

app.add_middleware(StarceptionMiddleware)  # must be the first one!

class User(BaseModel):
    username: str
    email: EmailStr

class UserCreate(BaseModel):
    username: str = None
    password: str = None
    email: Optional[EmailStr] = None

@app.get('/')
async def root():
    return {"message": "Hello World"}


@app.post('/register', response_model=User)
def register(user: UserCreate = Depends()):
    user = register_user(*user.dict().values())
    return user

# @app.post('/logout')
# def logout(request):
#     logout_user(request)
#     return True
    



@app.post('/token')
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=60)
    return {
        'access_token': create_access_token(
            data={'username': user.username}, expires_delta=access_token_expires
        ),
        'token_type': 'bearer',
    }

@app.post('/token/refresh')
def refresh_token(token: str = Depends(oauth2_scheme)):
    return {
        'access_token': create_refresh_token(
            data={'username': token['username']}
        ),
        'token_type': 'bearer',
    }





app.mount('/django', WSGIMiddleware(django_app))
app.include_router(store_router, prefix='/api', tags=['store'], dependencies=[Depends(oauth2_scheme)])
