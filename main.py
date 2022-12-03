from data_manager import *
from flight_search import *
from flight_data import FlightData

data_manager = DataManager()
sheet_data = data_manager.read_sheety()

flight_search = FlightSearch()

if sheet_data[0]["iataCode"] == '':
    for row in sheet_data:
        row["iataCode"] = flight_search.get_iata_code(row["city"])

data_manager.destination_data = sheet_data
data_manager.edit_sheety()
user_data = data_manager.read_users()
users = []

for row in user_data:
    email = (row["email"])
    name = (row["firstName"])
    users.append(email)


for row in sheet_data:
    flight = flight_search.get_flights(row["iataCode"])
    low_price = row["lowestPrice"]
    low_destination = row["iataCode"]
    flight_data = FlightData(flight, low_price, low_destination)
    flight_data.each_flight(users)


# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.