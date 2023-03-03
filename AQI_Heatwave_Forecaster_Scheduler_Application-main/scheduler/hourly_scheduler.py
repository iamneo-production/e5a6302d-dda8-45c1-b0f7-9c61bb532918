import pandas as pd
import numpy as np
from datetime import datetime, date
from io import StringIO
import datetime
import os
from scrapper import ScrapeAqiWeather
import warnings
warnings.filterwarnings("ignore")

cities = ['Adilabad', 'Nizamabad', 'Warangal', 'Karimnagar', 'Khammam']
bucket_name = 'capegemini-hackathon'
aqi_dataframes = {}
weather_dataframes = {}
URL_MAPPING = {'Adilabad': 'https://www.aqi.in/dashboard/india/telangana/adilabad',
               'Nizamabad': 'https://www.aqi.in/dashboard/india/telangana/nizamabad',
               'Khammam': 'https://www.aqi.in/dashboard/india/telangana/khammam',
               'Warangal': 'https://www.aqi.in/dashboard/india/telangana/warangal',
               'Karimnagar': 'https://www.aqi.in/dashboard/india/telangana/karimnagar'
               }


def create_excel_files(aqi_dataframes, weather_datframes, current_time):
    hour = current_time.hour
    with pd.ExcelWriter('/home/ec2-user/scheduler/data/daily_scrapped/aqi/AQI-Daily-{}-{}H.xlsx'.format(date.today(), hour)) as writer:
        for key, value in aqi_dataframes.items():
            value.to_excel(writer, sheet_name=key, index=False, header=True)
    with pd.ExcelWriter('/home/ec2-user/scheduler/data/daily_scrapped/weather/Weather-Daily-{}-{}H.xlsx'.format(date.today(), hour)) as writer:
        for key, value in weather_dataframes.items():
            value.to_excel(writer, sheet_name=key, index=False, header=True)


def delete_all_files_in_directory(dir_path):
    files = os.listdir(dir_path)
    for file in files:
        file_path = os.path.join(dir_path, file)
        if os.path.isfile(file_path):
            os.remove(file_path)


if __name__ == "__main__":
    try:
        print("\tHourly Scheduler")
        print("\t", datetime.datetime.now())
        for city in cities:
            print("******* City - {} ********".format(city))
            # Scrape New data from AQI DASHBOARD
            obj = ScrapeAqiWeather(URL_MAPPING[city], city)
            aqi_scrapped, weather_scrapped = obj.scrape_from_url()
            aqi_dataframes[city] = aqi_scrapped
            weather_dataframes[city] = weather_scrapped
        current_time = datetime.datetime.now().time()
        morning_threshold = datetime.time(hour=0, minute=30, second=0)
        if current_time < morning_threshold:
            delete_all_files_in_directory(
                '/home/ec2-user/scheduler/data/daily_scrapped/aqi')
            delete_all_files_in_directory(
                '/home/ec2-user/scheduler/data/daily_scrapped/weather')
        create_excel_files(aqi_dataframes, weather_dataframes, current_time)
    except Exception as e:
        print(e)
