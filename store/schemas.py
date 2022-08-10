from typing import Optional

from djantic import ModelSchema

from .models import Item, UpdateItem


class ItemCreateSchema(ModelSchema):
    
    slug: Optional[str] = None

    class Config:
        model = Item
        include = [
            'name',
            'price',
            'description',
            'image',
        ]

class ItemUpdateSchema(ModelSchema):
    
    slug: Optional[str] = None

    class Config:
        model = UpdateItem
        include = [
            'name',
            'price',
            'description',
            'image',
        ]
