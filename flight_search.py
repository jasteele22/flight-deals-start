import requests
import datetime

API_KEY = "te1D9fbNT68of8sqE-4-dz4TK0WcUwK2"
API_ENDPOINT = "https://api.tequila.kiwi.com/"

class FlightSearch:

    def __init__(self):
        self.header = {
            "apikey": API_KEY
        }
        today = datetime.datetime.now()
        tomorrow = today + datetime.timedelta(days=1)
        six_months = tomorrow + datetime.timedelta(days=30 * 6)
        self.from_date = tomorrow.strftime("%d/%m/%Y")
        self.to_date = six_months.strftime("%d/%m/%Y")


    def get_iata_code(self, city_name):
        query = {
            "term": city_name.upper(),
            "location_types": "city"
        }
        response = requests.get(url=f"{API_ENDPOINT}locations/query", headers=self.header, params=query)
        results = response.json()['locations']
        code = results[0]["code"]
        return code


    def get_flights(self, iataCode):
        query = {
            "fly_from": "RDU",
            "fly_to": iataCode,
            "date_from": self.from_date,
            "date_to": self.to_date,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "curr": "USD",
            "vehicle_type": "aircraft",
            "max_stop_overs": 3,
        }
        response = requests.get(url=f"{API_ENDPOINT}v2/search", headers=self.header, params=query)
        flights = response.json()["data"]
        for flight in flights:
            departure_iata = flight["cityCodeFrom"]
            departure_city = flight["cityFrom"]
            city_to = flight['cityTo']
            arrival_iata = flight['cityCodeTo']
            price = flight['price']
            leave_date = flight['route'][0]['local_departure'].split("T")[0]
            try:
                return_date = flight['route'][len("route") - 1]['local_departure'].split("T")[0]
            except IndexError:
                return_date = "N/A"
            deep_link = flight["deep_link"]
            message = f"{departure_iata}/{departure_city} to {arrival_iata}/{city_to}: ${price}.  This flight leaves on {leave_date} and returns on {return_date}.\n link: {deep_link}"
            return departure_iata, departure_city, city_to, arrival_iata, price, leave_date, return_date, deep_link, message
