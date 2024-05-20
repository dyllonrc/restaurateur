from fastapi import APIRouter
from ..services.restaurant_service import RestaurantService


router = APIRouter(
    prefix="/restaurants"
)

@router.get("/")
def read_restaurants():
    return
