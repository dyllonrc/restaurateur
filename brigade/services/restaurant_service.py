from ..db.DBObject import DBObject

class RestaurantService:

    def __init__(self, dbObj: DBObject):
        self.dbObj = dbObj
        return
