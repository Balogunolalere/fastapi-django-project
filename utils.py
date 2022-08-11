from django.contrib import auth
from django.contrib.auth.models import User
from datetime import timedelta, time
from django.conf import settings
import jwt


def register_user(username: str, password: str, email: str):
    user = User.objects.create_user(username=username, password=password, email=email)
    return user

# def logout_user(request):
#     auth.logout(request)
#     return True

def authenticate_user(username: str, password: str):
    user = auth.authenticate(username=username, password=password)
    if not user:
        return False
    return user


def create_access_token(*, data: dict, expires_delta: timedelta):
    data['exp'] = str(time()) + str(expires_delta.total_seconds())
    return jwt.encode(data, settings.SECRET_KEY, algorithm='HS256')


def create_refresh_token(*, data: dict, expires_delta: timedelta):
    data['exp'] = time() + expires_delta.total_seconds()
    return jwt.encode(data, settings.SECRET_KEY, algorithm='HS256')