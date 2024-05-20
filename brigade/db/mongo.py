from pymongo import MongoClient

from .DBObject import DBObject

class WalkenMongoClient(DBObject):
    def __init__(self, conn_str):
        self.client = MongoClient(conn_str)
        self.db = self.client['walken']
        print(f"Initialized client: {self.client}")

    def get_restaurants(self):
        return self.db['restaurants'].find()

    def close(self):
        self.client.close()
