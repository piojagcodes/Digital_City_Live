import requests
from typing import Dict

class WeatherService:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_weather_data(self, city: str) -> Dict:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}'
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception('Error fetching data')
        return response.json()


class WeatherReport:
    def __init__(self, weather_data: Dict):
        self.weather_data = weather_data

    def get_weather_description(self) -> str:
        return self.weather_data['weather'][0]['description']

    def get_city_longitude(self) -> float:
        return self.weather_data['coord']['lon']

    def get_city_latitude(self) -> float:
        return self.weather_data['coord']['lat']

    def get_wind_speed(self) -> float:
        return self.weather_data['wind']['speed']


def print_weather_report(report: WeatherReport) -> None:
    print("City longitude: {}".format(report.get_city_longitude()))
    print("City latitude: {}".format(report.get_city_latitude()))
    print("Today's weather will have: {}".format(report.get_weather_description()))
    print("Wind speed result: {}".format(report.get_wind_speed()))


def main():
    api_key = 'YOUR_API_KEY_HERE'
    city = input('Enter your city: ')

    weather_service = WeatherService(api_key)
    weather_data = weather_service.get_weather_data(city)

    report = WeatherReport(weather_data)
    print_weather_report(report)


if __name__ == '__main__':
    main()
