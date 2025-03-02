
from pony.orm import Database, Required,Json

db = Database()

class City(db.Entity):
    name = Required(str)
    total_crimes = Required(int)
    Crimes = Required(Json)