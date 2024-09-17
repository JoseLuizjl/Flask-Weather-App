# Flask-Weather-App


This project is a simple weather application built with Flask that allows users to search for the current weather in any city and country. It uses a geolocation API to retrieve the latitude and longitude of a city, and the OpenWeatherMap API to fetch the current weather data.

### Features:
- Search for the current weather by entering the country and city.
- Display temperature (current, min, and max) along with other weather details such as humidity and wind speed.
- Dynamic weather icons (GIFs) based on the weather condition.

### Technologies:
- **Flask**: Web framework for Python.
- **Bootstrap**: For a responsive and clean UI.
- **API Ninjas**: Geolocation API to get the latitude and longitude of a location.
- **OpenWeatherMap API**: Weather data provider.

### Installation:

1. Install the required dependencies:
   ```bash
   pip install python-dotenv
   pip install flask
   ```

2. Create a `.env` file in the root of the project and add the following API keys:
   ```bash
   API_KEY = "YourGeolocationAPIKey"
   API_KEY2 = "YourWeatherAPIKey"
   ```

   - To get the **Geolocation API Key**, visit [API Ninjas - Geocoding](https://api-ninjas.com/api/geocoding).
   - To get the **Weather API Key**, sign up at [OpenWeatherMap](https://openweathermap.org/).

3. Run the application:
   ```bash
   python app.py
   ```

### Usage:
Enter the country and city name in the input fields, and the app will display the current weather, temperature range, humidity, and wind speed for the specified location.

### APIs Used:

- **Geolocation API**: [API Ninjas - Geocoding](https://api-ninjas.com/api/geocoding)
- **Weather API**: [OpenWeatherMap](https://openweathermap.org/)


---