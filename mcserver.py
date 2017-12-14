# python mcserver.py

import configparser, logging, datetime, os, json, requests

import numpy as np

from flask import Flask, render_template, request

CONFIG_FILE = 'settings.config'
basedir = os.path.dirname(os.path.realpath(__file__))

# load the settings file
config = configparser.ConfigParser()
config.read(os.path.join(basedir, 'settings.config'))

# set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logging.info("Starting the MediaCloud example Flask app!")

# clean a mediacloud api client
weather_key = config.get('auth','api_key')

app = Flask(__name__)

# this tutorial has been pretty helpful https://www.dataquest.io/blog/python-api-tutorial/
# graphing was taken from the following Highcharts demo - http://jsfiddle.net/gh/get/library/pure/highcharts/highcharts/tree/master/samples/highcharts/demo/line-basic/
@app.route("/")
def home():
    # consider trying to use hermes cache to store weather data rather than calling the API, or store in a database

    # fetch data from the weather api

    base_url = "http://api.openweathermap.org/data/2.5/forecast?lat=42.37&lon=71.12&units=metric&APPID=" + weather_key
    print(base_url)
    #parameters = {'lat':42.36,'lon':71.058}
    #response = requests.get(base_url, params=parameters)
    response = requests.get(base_url)
    print('response state = ' + str(response))


    # extract temperature today and tomorrow

    weather_data = response.json()
    #print(weather_data)
    date_time1 = weather_data["list"][0]["dt_txt"]
    date_time2 = weather_data["list"][8]["dt_txt"]
    temp_today = weather_data["list"][0]["main"]["temp"]
    temp_tomorrow = weather_data["list"][8]["main"]["temp"]
    print("From " + str(date_time1) + " to " + str(date_time2))
    print("Temperature now " + str(temp_today) + ", temperature tomorrow " + str(temp_tomorrow))

    # extracting data for visualisation
    today_temp_array = []
    tomorrow_temp_array = []
    for i in range(8):
        today_temp_array.append(weather_data["list"][i]["main"]["temp"])
        tomorrow_temp_array.append(weather_data["list"][i+8]["main"]["temp"])

    weather_to_plot = [[0,1,2,3,4,5,6,7],today_temp_array,tomorrow_temp_array]

    # use weather data to figure out the change in temperature
    sum_today = 0;
    sum_tomorrow = 0;
    for i in range(len(today_temp_array)):
        sum_today += today_temp_array[i]
        sum_tomorrow += tomorrow_temp_array[i]
    average_today = sum_today/len(today_temp_array)
    average_tomorrow = sum_tomorrow/len(today_temp_array)

    difference = average_today - average_tomorrow
    if difference > 0:
        phrase = "colder than"
    elif difference < 0:
        phrase = "hotter than"
    else:
        phrase = "about the same as"
    return render_template("weather-results.html",
                           phrase=phrase,
                           number=9,
                           graphData=weather_to_plot)


if __name__ == "__main__":
    app.debug = True
    app.run()
