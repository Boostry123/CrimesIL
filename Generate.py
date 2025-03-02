import pandas as pd
from pony.orm import *
from visuals.Functions.models import *
import os

#This is a script that will take a CSV file and convert it into a database file using Pony ORM, and then export the data back into a new CSV file.

# Define the path to the database file
DB_FILE = 'CSV_Files/crimes.pony.db'
CRIMES_FILE = 'CSV_Files/crimes2024_new.csv'

# Check if the database file exists and remove it if it does
if os.path.exists(DB_FILE):
    os.remove(DB_FILE)
if os.path.exists(CRIMES_FILE):
    os.remove(CRIMES_FILE)


# Taking the Path to our CSV file and making a new pandas DataFrame
DB_PATH = 'CSV_Files/crimes2024_csv.csv'
df = pd.read_csv(DB_PATH, index_col="city")

db.bind(provider='sqlite', filename=DB_FILE, create_db=True)

set_sql_debug(False)
db.generate_mapping(create_tables=True)

cities = []
with db_session:
    for idx, row in df.iterrows():
        crime_data = {row['crimeType']: row['Crimes']}
        
        city_exist = City.get(name=idx)

        if city_exist:
            city_exist.total_crimes = city_exist.total_crimes + row['Crimes']
            city_exist.Crimes.update(crime_data)
        else:
            temp = City(name=idx, total_crimes=row['Crimes'], Crimes=crime_data)
            cities.append(temp)

# Here we will create a new organized DataFrame to export as a CSV
dataSet = {
    'City': [],
    'Total Crimes': [],
    'Crime List': []
}
new_df = pd.DataFrame(dataSet)
for city in cities:
    data = {'City': city.name, 'Total Crimes': city.total_crimes, 'Crime List': city.Crimes}
    new_df = new_df._append(data, ignore_index=True)
new_df.to_csv("CSV_Files/crimes2024_new.csv", encoding='utf-8-sig', index=False, header=True)



