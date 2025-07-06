import requests

API_Key = '1e0b460baa8540954811f65d97ab3c8d'


def get_weather(city):
    try:
        city_coordinates = requests.get(url=f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={API_Key}")

        data = city_coordinates.json()[0]

        lon = data['lon']
        lat = data['lat']

        city_weather = requests.get(
        url=f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={API_Key}")

        weather_result = city_weather.json()

        description,temp,feels_like = weather_result["weather"][0]["description"],weather_result["main"]["temp"],weather_result["main"]["feels_like"]

        return (f"The city of {city} has a temperature of {temp} °C and feels like it's {feels_like} °C. The weather conditions are: {description}")
    except ValueError:
        return (f"The city of {city} is not available")


