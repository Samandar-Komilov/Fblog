from typing import Annotated
from fastapi.routing import APIRouter
from fastapi import Path

router = APIRouter(prefix="/items")

@router.get("/latest")
def latest():
    return {"item": {"id":0, "name":"latest"}}


@router.get("/{item_id}/")
def get_item(item_id: Annotated[int, Path(gt=0, lt=1_000_000)]):
    return {
        "item": {
            "id": item_id
        }
    }