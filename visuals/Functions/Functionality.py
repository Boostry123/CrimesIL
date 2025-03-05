from pony.orm import db_session, desc
from visuals.Functions.models import db, City

# Ensure the database mapping is generated
db.bind(provider='sqlite', filename='F:\coding\Python\crimes\CSV_Files\crimes.pony.db', create_db=False)
db.generate_mapping()


# Function to fetch the top 10 cities by total crimes
@db_session
def topTen():
    try:
        with db_session:
            # Fetch the first 10 cities
            cities = City.select().order_by(lambda c: desc(c.total_crimes))[:10]
            return cities
    except Exception as e:
        print(f"Error fetching top 10 cities: {e}")
        return []

# Fetch the first 5 cities by total crimes
def topFive():
    try:
        with db_session:
            # Fetch the first 5 cities
            cities = City.select().order_by(lambda c: desc(c.total_crimes))[:5]
            return cities
    except Exception as e:
        print(f"Error fetching top 5 cities: {e}")
        return []

# Fetch all City names
def cityNames():
    try:
        with db_session:
            cities = City.select()
            city_names = [city.name[::-1] for city in cities]  # Reverse the text for Hebrew
            return city_names
    except Exception as e:
        print(f"Error fetching city names: {e}")
        return []
    