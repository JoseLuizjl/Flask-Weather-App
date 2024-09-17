from flask import Flask, render_template, request, redirect, url_for
from weather_api import get_weather, get_lan_lon

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['cityName']
        country = request.form['countryName']
        
        lat, lon = get_lan_lon(city, country)
        temperature, temp_max, temp_min, humidity, wind, weather = get_weather(lat, lon)
        
        weather_data = {
            'city': city,
            'country': country,
            'temperature': temperature,
            'temp_max': temp_max,
            'temp_min': temp_min,
            'humidity': humidity,
            'wind': wind,
            'weather': weather
        }
        
        return redirect(url_for('index', **weather_data))
    
    weather_data = {
        'city': request.args.get('city'),
        'country': request.args.get('country'),
        'temperature': request.args.get('temperature'),
        'temp_max': request.args.get('temp_max'),
        'temp_min': request.args.get('temp_min'),
        'humidity': request.args.get('humidity'),
        'wind': request.args.get('wind'),
        'weather': request.args.get('weather'),
    }
    
    return render_template('index.html', **weather_data)

if __name__ == "__main__":
    app.run(debug=True)
