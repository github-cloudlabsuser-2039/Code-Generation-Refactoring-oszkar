import requests

def fetch_weather(city_name, api_key):
    """
    Fetch weather data for a given city from OpenWeatherMap API.

    Args:
        city_name (str): Name of the city to fetch weather for.
        api_key (str): Your OpenWeatherMap API key.

    Returns:
        dict: Weather data if successful, or an error message.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

if __name__ == "__main__":
    # Replace with your OpenWeatherMap API key
    API_KEY = "your_api_key_here"
    city = input("Enter the city name: ")

    weather_data = fetch_weather(city, API_KEY)

    if "error" in weather_data:
        print(f"Error: {weather_data['error']}")
    else:
        print(f"Weather in {weather_data['name']}:")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Weather: {weather_data['weather'][0]['description'].capitalize()}")
        print(f"Humidity: {weather_data['main']['humidity']}%")