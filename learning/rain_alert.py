import requests
import os

latitude = 46.235420
longitude = -63.126518

weather_params = {
    "lat": latitude,
    "lon": longitude,
    "appid": os.environ.get("OWM_API_KEY"),
    "cnt": 4
}


def is_rainy_weather():
    for hourly_weather in weather_dict.get("list"):
        weather = hourly_weather.get("weather")
        for data in weather:
            if data.get("id") < 700:
                return True

    return False


response = requests.get("http://api.openweathermap.org/data/2.5/forecast", params=weather_params)
response.raise_for_status()
weather_dict = response.json()

if is_rainy_weather():
    print ("Bring an Umbrella")
