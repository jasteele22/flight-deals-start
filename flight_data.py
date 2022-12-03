from notification_manager import NotificationManager

API_KEY = "te1D9fbNT68of8sqE-4-dz4TK0WcUwK2"
API_ENDPOINT = "https://api.tequila.kiwi.com/"

class FlightData:
    def __init__(self, flight, low_price, low_destination):
        self.messages = []
        self.low_price = low_price
        self.low_destination = low_destination
        try:
            self.flight = flight
            self.price = self.flight[4]
            self.message = self.flight[8]
        except TypeError:
            print(f"No flights found for {low_destination}")
            self.price = 1000000

    def each_flight(self, users):
        if self.price < self.low_price:
            text = NotificationManager(self.message)
            for user in users:
                text.send_email(user)


