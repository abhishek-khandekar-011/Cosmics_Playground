import os
import requests
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

API_KEY = os.environ.get("OWM_API_KEY")
ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_NUMBER = os.environ.get("TWILIO_PHONE_NUMBER")
TO_NUMBER = os.environ.get("MY_PHONE_NUMBER")

# OpenWeatherMap API Setup
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
weather_params = {
    "lat": 19.075983,
    "lon": 72.877655,
    "appid": API_KEY,
    "cnt": 4,
}

response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
data = response.json()

will_rain = False

for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 600:
        will_rain = True
        break

if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body="It's going to rain today. Remember to carry an umbrella! ☔",
        from_=TWILIO_NUMBER,
        to=TO_NUMBER,
    )
    print(f"Message sent! Status: {message.status}")
else:
    print("No rain expected in the upcoming forecast hours.")