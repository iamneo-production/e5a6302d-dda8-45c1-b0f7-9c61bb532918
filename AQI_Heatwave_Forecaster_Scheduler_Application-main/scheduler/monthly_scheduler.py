import pandas as pd
import numpy as np
import numpy as np
import boto3
from datetime import datetime,date
from io import StringIO
import os
from scrapper import ScrapeAqiWeather
from LSTM_RNN import LSTM_Model 
from datetime import date
import warnings
warnings.filterwarnings("ignore")

cities=['Adilabad','Nizamabad','Warangal','Karimnagar','Khammam']
bucket_name = 'capegemini-hackathon'
aqi_dataframes={}
weather_dataframes={}
AQI_MONTHLY_DATA_PATH='s3://capegemini-hackathon/data/aqi/monthly/aqi-monthly.xlsx'
WEATHER_MONTHLY_DATA_PATH='s3://capegemini-hackathon/data/weather/monthly/weather-monthly.xlsx'
URL_MAPPING = {'Adilabad': 'https://www.aqi.in/dashboard/india/telangana/adilabad',
                   'Nizamabad': 'https://www.aqi.in/dashboard/india/telangana/nizamabad',
                   'Khammam': 'https://www.aqi.in/dashboard/india/telangana/khammam',
                   'Warangal': 'https://www.aqi.in/dashboard/india/telangana/warangal',
                   'Karimnagar': 'https://www.aqi.in/dashboard/india/telangana/karimnagar'
                   }

def get_weather_and_aqi_data(city):
  aqi_df= pd.read_excel(AQI_MONTHLY_DATA_PATH,sheet_name=city,header=0)
  weather_df = pd.read_excel(WEATHER_MONTHLY_DATA_PATH,sheet_name=city,header=0)
  return aqi_df,weather_df

def create_date_values(start_date,count,freq):
    print("Start Time:",start_date)
    print("Type:",type(start_date),'\n')
    start_date=pd.to_datetime(start_date, infer_datetime_format=True)
    if freq=='D':
        datelist = pd.date_range(start=start_date, periods=count, freq='D')
        return datelist
    else:
        monthlist = pd.date_range(start=start_date, periods=count, freq='MS')
        return monthlist

def create_dataframe(data,start_date,count,freq):
    date=create_date_values(start_date,count,freq)
    df_data=[date,data[0]]
    df=pd.DataFrame(df_data).transpose()
    df.columns=['Date','Predictions']
    return df

def create_excel_files(aqi_dataframes, weather_datframes):
    with pd.ExcelWriter(AQI_MONTHLY_DATA_PATH) as writer:
        for key,value in aqi_dataframes.items():
            value.to_excel(writer, sheet_name=key,index=False,header=True)
    with pd.ExcelWriter(WEATHER_MONTHLY_DATA_PATH) as writer:
        for key,value in weather_dataframes.items():
            value.to_excel(writer, sheet_name=key,index=False,header=True)

def train_lstm_model(data,parameter_type):
  print(data.tail())
  model=LSTM_Model(50,1)
  model.load_data(data,parameter_type)
  model.execute()
  return model

def get_start_date(data):
  start_date=(data['DATE'].iloc[-1]+ pd.offsets.MonthEnd(0) + pd.DateOffset(days=1)).date()
  return start_date

def get_forecasted_values(model,forecast_horizon,start_date):
  forecasted_values = model.forecast_future(15)
  df=create_dataframe(forecasted_values.reshape(1,15).tolist(),start_date,15,'M')
  return df
 
def get_monthly_from_daily(city):
    aqi_daily=pd.read_excel('s3://capegemini-hackathon/data/aqi/daily/aqi-daily.xlsx',sheet_name=city,header=0)
    weather_daily=pd.read_excel('s3://capegemini-hackathon/data/weather/daily/weather-daily.xlsx',sheet_name=city,header=0)
    prev_month=(aqi_daily['DATE'].iloc[-1]-pd.offsets.MonthBegin(1)).month
    print("Prev Month",prev_month)
    last_month_aqi=aqi_daily.loc[aqi_daily['DATE'].dt.month==prev_month]
    last_month_weather=weather_daily.loc[weather_daily['DATE'].dt.month==prev_month]
    print("**AQI**")
    print(last_month_aqi.head())
    print("**Weather**")
    print(last_month_weather.head())
    last_month_aqi_data=last_month_aqi.mean(axis=0).to_frame().T
    last_month_aqi_data['DATE']=(pd.Timestamp.now()-pd.offsets.MonthBegin(1)).date()
    last_month_weather_data=last_month_weather.mean(axis=0).to_frame().T
    last_month_weather_data['DATE']=(pd.Timestamp.now()-pd.offsets.MonthBegin(1)).date()
    return last_month_aqi_data,last_month_weather_data

    
if __name__=="__main__":
    print("\Monthly Scheduler")
    print("\t",datetime.now())
    for city in cities:
        print("******* City - {} ********".format(city))
        aqi_data,weather_data=get_weather_and_aqi_data(city)
      #   print(aqi_data.head())
        #Scrape New data from AQI DASHBOARD
        obj = ScrapeAqiWeather(URL_MAPPING[city], city)
        aqi_scrapped, weather_scrapped = get_monthly_from_daily(city)
        aqi_data['DATE']=pd.to_datetime(aqi_data['DATE'])
        #-----AQI-----
        #Append new AQI data to historical data
        aqi_data=aqi_data.append(aqi_scrapped,ignore_index=True)
        aqi_data.fillna('-',inplace=True)
        #Train model for AQI daily predictions and forecast
        aqi_model = train_lstm_model(aqi_data,"AQI")
        start_date_forecast=get_start_date(aqi_data)
        aqi_forecasted = get_forecasted_values(aqi_model,15,start_date_forecast)
        print("***** AQI Forecast********")
        print(aqi_forecasted.head())
        # Upload the forecasted AQI csv to s3
        aqi_forecasted.to_csv('s3://capegemini-hackathon/monthly/aqi/{}/aqi-{}.csv'.format(city,str(datetime.now().strftime('%B')+'-'+datetime.now().strftime('%Y'))),index=False,header=True)

        #-------Weather--------

        #Append new Weather data to historical data
        weather_data=weather_data.append(weather_scrapped,ignore_index=True)
        weather_data.fillna('-',inplace=True)
        # train_weather=weather_data[['DATE','Max Temp (°C)']]
        #Train model for daily Weather predictions and forecast
        weather_model = train_lstm_model(weather_data,"Max Temp (°C)")
        start_date_forecast=get_start_date(weather_data)
        weather_forecasted = get_forecasted_values(weather_model,15,start_date_forecast)
        print("***** Weather Forecast********")
        print(weather_forecasted.head())
        # Upload the forecasted Weather csv to s3
        weather_forecasted.to_csv('s3://capegemini-hackathon/monthly/weather/{}/weather-{}.csv'.format(city,str(datetime.now().strftime('%B')+'-'+datetime.now().strftime('%Y')),index=False,header=True))
        #Store Updated Dataframes for each city
        aqi_dataframes[city]=aqi_data
        weather_dataframes[city]=weather_data
    #Store Updated Daframes to local    
    create_excel_files(aqi_dataframes,weather_dataframes)