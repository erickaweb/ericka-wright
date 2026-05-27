import requests

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 34.05,
    "longitude": -118.24,
    "current": "temperature_2m,wind_speed_10m",
    "temperature_unit": "fahrenheit"
}

response = requests.get(url, params=params)
data = response.json()

current = data["current"]
print(f"Temperature: {current['temperature_2m']}°F")
print(f"Wind Speed: {current['wind_speed_10m']} km/h")
print(f"Time: {current['time']}")