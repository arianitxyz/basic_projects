import requests
from pprint import pprint

API_Key = '8f73a96e9cb39fc0a142985c2929f216'

city = input("Enter a city: ")

base_url = "https://api.openweathermap.org/data/2.5/weather?appid=" + API_Key + "&q=" + city
print(base_url)
weather_data = requests.get(base_url).json()

pprint(weather_data)


