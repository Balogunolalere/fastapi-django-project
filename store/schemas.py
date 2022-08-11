from typing import Optional

from djantic import ModelSchema

from .models import Item


class ItemCreateSchema(ModelSchema):
    class Config:
        model = Item
        exclude = ('id', 'timestamp')

class ItemUpdateSchema(ModelSchema):
    class Config:
        model = Item
        exclude = ('id', 'timestamp', 'name', 'image', 'slug')
        load_only = ('price', 'description',)

class ItemSchema(ModelSchema):
    class Config:
        model = Item