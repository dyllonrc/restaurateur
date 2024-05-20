from contextlib import asynccontextmanager
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from dotenv import load_dotenv

from db.mongo import WalkenMongoClient

load_dotenv()
conn_str = os.environ["WALKEN_CONN_STR"]

print(conn_str)

dbClient = WalkenMongoClient(conn_str)
for item in dbClient.get_restaurants():
    print(item)

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

@asynccontextmanager
async def lifespan(app: FastAPI):
    pass


app = FastAPI()

origins = [
    "http://localhost:5173"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins
)


@app.get("/")
def read_root():
    return sampleData
