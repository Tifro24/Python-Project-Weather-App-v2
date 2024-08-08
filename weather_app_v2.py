import requests
from dotenv import load_dotenv
import os
load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
city = "Hawaii"

def kelvin_to_celsius_farenheight(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) +32
    return celsius, fahrenheit

url = BASE_URL + "appid=" + API_KEY + "&q=" + city

response = requests.get(url).json()
print(response)

city_name = response['name']
temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = kelvin_to_celsius_farenheight(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_farenheight(feels_like_kelvin)
conditions = response['weather'][0]['main'] + " - " + response['weather'][0]['description']
wind_speed = response['wind']['speed'] + "km/h"
humidity = response['main']['humidity']