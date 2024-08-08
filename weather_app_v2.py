import datetime as dt
import requests
from dotenv import load_dotenv
import os
load_dotenv()

API_KEY = os.getenv("API_KEY")



BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
city = "london"

url = BASE_URL + "appid=" + API_KEY + "&q=" + city

response = requests.get(url).json()
print(response)


