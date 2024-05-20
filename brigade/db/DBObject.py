from abc import ABC, abstractmethod
from typing import Iterable

from pymongo.cursor import Cursor

class DBObject(ABC):

    @abstractmethod
    def get_restaurants(self) -> Iterable:
        pass
