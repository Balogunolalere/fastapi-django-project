
from typing import List
from datetime import datetime

from fastapi import APIRouter

from store.models import Item
from store.schemas import ItemCreateSchema, ItemUpdateSchema



router = APIRouter()


@router.post('/items/', response_model=ItemCreateSchema, status_code=201)
def create_item(item: ItemCreateSchema):
    page = Item.objects.create(**item.dict())
    return ItemCreateSchema.from_django(page)


@router.get('/items/', response_model=List[ItemCreateSchema])
def read_items():
    return ItemCreateSchema.from_django(Item.objects.all(), many=True)

@router.put('/items/{item_id}', response_model=ItemUpdateSchema)
def update_item(item_id: int, item: ItemUpdateSchema):
    page = Item.objects.get(id=item_id)
    page.name = item.name
    page.price = item.price
    page.description = item.description
    page.image = item.image
    timestamp = str(datetime.now().timestamp())
    # save timestamp to database
    page.timestamp = timestamp
    page.save()
    return ItemUpdateSchema.from_django(page)




