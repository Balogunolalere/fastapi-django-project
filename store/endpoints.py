
from typing import List
from datetime import datetime

from fastapi import APIRouter

from store.models import Item
from store.schemas import ItemCreateSchema, ItemUpdateSchema, ItemSchema



router = APIRouter()


@router.post('/items/', response_model=ItemSchema, status_code=201)
def create_item(item: ItemCreateSchema):
    page = Item.objects.create(**item.dict())
    return ItemSchema.from_django(page)


@router.get('/items/', response_model=List[ItemSchema])
def read_items():
    return ItemSchema.from_django(Item.objects.all(), many=True)

@router.put('/items/{item_id}', response_model=ItemSchema)
def update_item(item_id: int, item: ItemUpdateSchema):
    page = Item.objects.get(id=item_id)
    # only update fields with new values
    for field, value in item.dict().items():
        setattr(page, field, value)
    page.save()
    return ItemSchema.from_django(page)



