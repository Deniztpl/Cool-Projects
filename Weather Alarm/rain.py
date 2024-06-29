# Add environment variables OWM_API_KEY and AUTH_TOKEN

import os
import requests
from twilio.rest import Client

api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACC_SID")
auth_token = os.environ.get("AUTH_TOKEN")

params = {
    'lat': 41.008240,
    'lon': 28.978359,
    'cnt': 4,
    'appid': api_key
}

response = requests.get('https://api.openweathermap.org/data/2.5/forecast', params=params)

response.raise_for_status()
data = response.json()

def rainy_weather(x):
    if int(x['weather'][0]['id']) < 700:
        return True

for hour in data['list']:
    if rainy_weather(hour):

        client = Client(account_sid, auth_token)

        message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔",
        from_="+13613169836",
        to="+90 538 266 71 79",
        )
        print(message.status)
        break

