from twilio.rest import Client
import smtplib
import datetime as dt

MY_EMAIL = "justinsteelepython@gmail.com"
PASSWORD = "nsgb hvkg ldxl hizg"
DATE = dt.datetime.now()
today = f"{DATE.day}/{DATE.month}/{DATE.year}"
six_months = DATE + dt.timedelta(days=30 * 6)
six_months_date = f"{six_months.day}/{six_months.month}/{six_months.year}"


class NotificationManager:

    def __init__(self, messages):
        self.account_sid = 'AC821a248f8a483fcaa20d40d3b2de7cf2'
        self.auth_token = 'e99fccbec1019b00e16edb3b5c240f5d'
        self.message = messages

    def send_text(self):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages \
            .create(
            body= self.message,
            from_='+12488261778',
            to='+19312654874'
        )
        print(message.status)

    def send_email(self, user_email):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=user_email,
                msg = f"Subject:Travel Deals {today} to {six_months_date}\n\n {self.message}")


    #This class is responsible for sending notifications with the deal flight details.
