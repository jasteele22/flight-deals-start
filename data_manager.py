import requests
from pprint import pprint
FLIGHT_DATA_ENDPOINT = "https://api.sheety.co/fa3ec60ca47533d1462c4d44fff7e675/flightDeals/prices"
FLIGHT_DATA_USERS = "https://api.sheety.co/fa3ec60ca47533d1462c4d44fff7e675/flightDeals/users"
TOKEN = "Bearer xtuRFrbPRULnmUd2MtMW"

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.destination_data = {}
        self.data_headers = {
            "Authorization": TOKEN,
        }

    def read_sheety(self):
        response = requests.get(url=FLIGHT_DATA_ENDPOINT, headers=self.data_headers)
        data = response.json()
        self.destination_data = data["prices"]

        return self.destination_data

    def read_users(self):
        response = requests.get(url=FLIGHT_DATA_USERS, headers=self.data_headers)
        data = response.json()
        self.user_data = data["users"]

        return self.user_data


    def edit_sheety(self):
        for city in self.destination_data:
            data_params = {
                'price': {
                    'iataCode': city['iataCode']
                }
            }
            response = requests.put(url=f"{FLIGHT_DATA_ENDPOINT}/{city['id']}", headers=self.data_headers, json=data_params)