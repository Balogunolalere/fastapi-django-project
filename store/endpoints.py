
from typing import List
from datetime import datetime

from fastapi import APIRouter

from store.models import Item
from store.schemas import ItemCreateSchema, ItemUpdateSchema, ItemSchema



router = APIRouter()


@router.post('/items/', response_model=ItemSchema, status_code=201, summary='Create an  item')
def create_item(item: ItemCreateSchema):
    page = Item.objects.create(**item.dict())
    return ItemSchema.from_django(page)


@router.get('/items/', response_model=List[ItemSchema], status_code=200, summary='List all items')
def read_items():
    return ItemSchema.from_django(Item.objects.all(), many=True)

@router.get('/items/{item_slug}', response_model=ItemSchema, status_code=200, summary='Read an item')
def read_item(item_slug: str):
    return ItemSchema.from_django(Item.objects.get(slug=item_slug))

@router.put('/items/{item_id}', response_model=ItemSchema, status_code=200, summary='Update an item')
def update_item(item_id: int, item: ItemUpdateSchema):
    page = Item.objects.get(id=item_id)
    # only update fields with new values
    for field, value in item.dict().items():
        setattr(page, field, value)
    page.save()
    return ItemSchema.from_django(page)



