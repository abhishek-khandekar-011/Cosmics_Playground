import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/58428ea9f43d2b0a41aa246379ff31bc/flightDeals/prices"


class DataManager:

    def __init__(self):
        self._user = os.environ["Cosmic999"]
        self._password = os.environ["#&3373*#@&239z"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, auth=self._authorization)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data
