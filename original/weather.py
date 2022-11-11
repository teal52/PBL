import json
import requests


url="https://www.jma.go.jp/bosai/forecast/data/forecast/080000.json"

'''
weather_data = requests.get(url).json()

weather_date = weather_data[0]["timeSeries"][0]["timeDefines"][0]
weather_weather = weather_data[0]["timeSeries"][0]["areas"][0]["weathers"][0]
'''

proxies = {
    'http':'http://po.cc.ibaraki-ct.ac.jp:3128',
    'https':'http://po.cc.ibaraki-ct.ac.jp:3128'
}


def get_json():
    weather_data = requests.get(url).json()

    weather_date = weather_data[0]["timeSeries"][0]["timeDefines"][0]
    weather_weather = weather_data[0]["timeSeries"][0]["areas"][0]["weathers"][0]

    weather_weather = weather_weather.replace('　','')


    data_box={"date":weather_date,"weather":weather_weather}

    return data_box

'''
a = get_json()
print(a["weather"])


weather_rainfall = weather_data["Feature"][0]["Property"]["WeatherList"]["Weather"][0]["Rainfall"]
'''







'''
https://www.gis-py.com/entry/weather-json
'''