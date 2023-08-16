from unittest.mock import MagicMock
import pytest
from coordinates import WeatherService, WeatherReport, print_weather_report


@pytest.fixture
def mock_weather_service():
    weather_service = WeatherService(api_key='TEST_API_KEY')
    weather_service.requests.get = MagicMock()
    return weather_service


def test_get_weather_data_returns_dict(mock_weather_service):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'weather': [{'description': 'sunny'}], 'coord': {'lon': -122.08, 'lat': 37.39}, 'wind': {'speed': 1.5}}
    mock_weather_service.requests.get.return_value = mock_response

    weather_data = mock_weather_service.get_weather_data(city='San Francisco')

    assert isinstance(weather_data, dict)


def test_get_weather_data_raises_exception_on_error(mock_weather_service):
    mock_response = MagicMock()
    mock_response.status_code = 404
    mock_weather_service.requests.get.return_value = mock_response

    with pytest.raises(Exception):
        mock_weather_service.get_weather_data(city='Invalid City')


@pytest.fixture
def mock_weather_report():
    weather_data = {'weather': [{'description': 'sunny'}], 'coord': {'lon': -122.08, 'lat': 37.39}, 'wind': {'speed': 1.5}}
    return WeatherReport(weather_data=weather_data)


def test_get_weather_description_returns_string(mock_weather_report):
    weather_description = mock_weather_report.get_weather_description()

    assert isinstance(weather_description, str)


def test_get_city_longitude_returns_float(mock_weather_report):
    city_longitude = mock_weather_report.get_city_longitude()

    assert isinstance(city_longitude, float)


def test_get_city_latitude_returns_float(mock_weather_report):
    city_latitude = mock_weather_report.get_city_latitude()

    assert isinstance(city_latitude, float)


def test_get_wind_speed_returns_float(mock_weather_report):
    wind_speed = mock_weather_report.get_wind_speed()

    assert isinstance(wind_speed, float)


def test_print_weather_report_prints_correctly(mock_weather_report):
    mock_weather_report.get_city_longitude.return_value = -122.08
    mock_weather_report.get_city_latitude.return_value = 37.39
    mock_weather_report.get_weather_description.return_value = 'sunny'
    mock_weather_report.get_wind_speed.return_value = 1.5

    with pytest.raises(StopIteration):
        with pytest.raises(StopIteration):
            with pytest.raises(StopIteration):
                with pytest.raises(StopIteration):
                    print_weather_report(mock_weather_report)
