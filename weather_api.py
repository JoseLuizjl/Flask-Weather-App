import requests
from dotenv import load_dotenv
import os


load_dotenv()
api_key = os.getenv('API_KEY')
api_key2 = os.getenv('API_KEY2')

def get_lan_lon(city_name, country):
    api_url = f'https://api.api-ninjas.com/v1/geocoding?city={city_name}&country={country}'
    response = requests.get(api_url, headers={'X-Api-Key': f'{api_key}'}).json()

    lat = response[0]['latitude']
    lon = response[0]['longitude']

    return lat, lon

def get_weather(lat, lon):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key2}&units=metric').json()
    
    temp = response['main']['temp']
    temp_max = response['main']['temp_max']
    temp_min = response['main']['temp_min']
    humidity = response['main']['humidity']
    wind = response['wind']['speed']
    weather = response['weather'][0]['main']
    
    return temp, temp_max, temp_min, humidity, wind, weather
