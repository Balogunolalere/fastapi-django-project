from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from django.core.wsgi import get_wsgi_application
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from fastapi.staticfiles import StaticFiles
from .endpoints import router



django_app = get_wsgi_application()

app = FastAPI() 

app.mount('/django/static', StaticFiles(directory='static'), name='static')

@app.get('/')
async def root():
    return {"message": "Hello World"}

app.mount('/django', WSGIMiddleware(django_app))
app.include_router(router, prefix='/api')
