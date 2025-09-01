# Simple weather app
import requests

city_name = input("Enter city name: ")

api_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1"

response = requests.get(api_url).json()

if "results" not in response:
    print("City not found")
else:
    lat = response["results"][0]["latitude"]
    lon = response["results"][0]["longitude"]

weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

weather_response = requests.get(weather_url).json()

temp = weather_response["current_weather"]["temperature"]
wind = weather_response["current_weather"]["windspeed"]

print(f"Current temperature in {city_name}: {temp}°C, Wind Speed: {wind} km/h")
