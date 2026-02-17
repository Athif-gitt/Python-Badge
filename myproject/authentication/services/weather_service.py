import requests
from django.conf import settings

def fetch_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={settings.API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json
    return response.raise_for_status()

