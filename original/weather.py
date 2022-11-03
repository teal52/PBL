import json
import requests


url="https://www.jma.go.jp/bosai/forecast/data/forecast/080000.json"


weather_data = requests.get(url).json()

weather_date = weather_data[0]["timeSeries"][0]["timeDefines"][0]
weather_weather = weather_data[0]["timeSeries"][0]["areas"][0]["weathers"][0]


weather_weather = weather_weather.replace('　','')



print(weather_weather)







'''
https://www.gis-py.com/entry/weather-json
'''