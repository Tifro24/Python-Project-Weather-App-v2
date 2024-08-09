import requests
from dotenv import load_dotenv
import os
load_dotenv()

API_KEY = os.getenv("API_KEY") # hid API key in .env file 
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

# Function to convert kevlin into celsius and fahrenheit
def kelvin_to_celsius_farenheight(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) +32
    return celsius, fahrenheit

# Welcome messsage
print('*'* 50)
print('           ','Welcome to the Weather App!')
print('*'* 50)
print('')

def weather_forecast():

    city = input("Please enter a city: ")

    # Concatenating the variables needed to form the url for the city we need our forecast from
    url = BASE_URL + "appid=" + API_KEY + "&q=" + city
    

    response = requests.get(url).json()
    
    # Accounting for inputs that arent found in the database or are invalid
    if 'city not found' in response.values():
        print("\nUnfortunately, either this city isn't in our database or it's invalid.\n")
        ans = input("Would you like to try again? Enter 'Yes' to continue or 'No' to exit: ")
        if ans.lower() == 'yes':
            print('')
            weather_forecast()
        elif ans.lower() == 'no':
            print("Thanks again and have a great day!")
            exit()
        else:
            print("That wasn't either of the options, but I'll take it as a no, have a great day!")
            exit()
    else:
        # creating variables for the values extracted from the dictionary 
        city = response['name']
        temp_kelvin = response['main']['temp']
        temp_celsius, temp_fahrenheit = kelvin_to_celsius_farenheight(temp_kelvin)
        feels_like_kelvin = response['main']['feels_like']
        feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_farenheight(feels_like_kelvin)
        conditions = response['weather'][0]['main']
        conditions_desc = response['weather'][0]['description']
        wind_speed = response['wind']['speed']
        humidity = response['main']['humidity']
        country = response['sys']['country']

        # print statements to format the display of the info to be presented to the user
        print(f"\n{city}")
        print(f"Temperature: {temp_celsius:.2f}°C or {temp_fahrenheit:.2f}°F")
        print(f"Feels Like: {feels_like_celsius:.2f}°C or {feels_like_fahrenheit:.2f}°F")
        print(f"Conditions: {conditions} - {conditions_desc}")
        print(f"Wind Speed: {wind_speed}km/h")
        print(f"Humidity: {humidity}%")
        print(f"Country: {country}")
        print("\nThank you for using the program!\n")

        # Allowing the user to either try again or exit the program, accounting for any inputs that aren't either yes or no.
        ans = input("Would you like to enter anothery city? Please enter Yes or No: ")
        if ans.lower() == 'yes':
            print('')
            weather_forecast()
        elif ans.lower() == 'no':
            print("Thanks again and have a great day!")
            exit()
        else:
            print("That wasn't either of the options, but I'll take it as a no, have a great day!")
            exit()

weather_forecast()