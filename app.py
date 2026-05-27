from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def weather():
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


    return f"""
<h1>LA Weather</h1>
<p>Temperature: {current['temperature_2m']}°F</p>
    <p>Wind Speed: {current['wind_speed_10m']} km/h</p>
    <p>Time: {current['time']}</p>
    """

if __name__ == "__main__":
    app.run(debug=True)