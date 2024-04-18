from fastapi import FastAPI

from pydantic import BaseModel

class RestaurantModel(BaseModel):
    name: str
    priceTier: str
    userRating: str

sampleData = [
    RestaurantModel(name="McDonald's", priceTier="$", userRating="3/5"),
    RestaurantModel(name="Five Guys", priceTier="$$", userRating="3.5/5"),
    RestaurantModel(name="Emmy Squared Pizzeria", priceTier="$$$", userRating="4/5"),
    RestaurantModel(name="Eleven Madison Park", priceTier="$$$$", userRating="4.9/5")
]

app = FastAPI()


@app.get("/")
def read_root():
    return sampleData
