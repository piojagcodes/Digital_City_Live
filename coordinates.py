import requests


city = input('Enter your city: ')



url = 'YOUR_API_KEY_HERE'.format(city)

res = requests.get(url)

data = res.json()



weather_data = data['weather'][0]['description']
lon = data['coord']['lon']
lat = data['coord']['lat']
wind_speed = data['wind']['speed']

print("City longitude: {}".format(lon))
print("City latitude: {}".format(lat))
print("Today's weather will have: {}".format(weather_data))
print("Wind speed result: {}".format(wind_speed))
