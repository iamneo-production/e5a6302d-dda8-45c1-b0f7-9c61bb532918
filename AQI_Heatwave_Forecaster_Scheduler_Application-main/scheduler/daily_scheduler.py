import pandas as pd
import numpy as np
import numpy as np
from datetime import datetime,date
from io import StringIO
import os
import datetime
from scrapper import ScrapeAqiWeather
from LSTM_RNN import LSTM_Model 
from datetime import date
import warnings
warnings.filterwarnings("ignore")

cities=['Adilabad','Nizamabad','Warangal','Karimnagar','Khammam']
bucket_name = 'capegemini-hackathon'
aqi_dataframes={}
weather_dataframes={}
AQI_DAILY_DATA_PATH='s3://capegemini-hackathon/data/aqi/daily/aqi-daily.xlsx'
WEATHER_DAILY_DATA_PATH='s3://capegemini-hackathon/data/weather/daily/weather-daily.xlsx'
URL_MAPPING = {'Adilabad': 'https://www.aqi.in/dashboard/india/telangana/adilabad',
                   'Nizamabad': 'https://www.aqi.in/dashboard/india/telangana/nizamabad',
                   'Khammam': 'https://www.aqi.in/dashboard/india/telangana/khammam',
                   'Warangal': 'https://www.aqi.in/dashboard/india/telangana/warangal',
                   'Karimnagar': 'https://www.aqi.in/dashboard/india/telangana/karimnagar'
                   }

def get_weather_and_aqi_data(city):
  aqi_df= pd.read_excel(AQI_DAILY_DATA_PATH,sheet_name=city,header=0)
  weather_df = pd.read_excel(WEATHER_DAILY_DATA_PATH,sheet_name=city,header=0)
  return aqi_df,weather_df

def create_date_values(start_date,count,freq):
    start_date=pd.to_datetime(start_date, infer_datetime_format=True)
    if freq=='D':
        datelist = pd.date_range(start=start_date, periods=count, freq='D')
        return datelist
    else:
        monthlist = pd.date_range(start=start_date, periods=count, freq='M')
        return monthlist

def create_dataframe(data,start_date,count,freq):
    date=create_date_values(start_date,count,freq)
    df_data=[date,data[0]]
    df=pd.DataFrame(df_data).transpose()
    df.columns=['Date','Predictions']
    return df

def create_excel_files(aqi_dataframes, weather_datframes):
    with pd.ExcelWriter(AQI_DAILY_DATA_PATH) as writer:
        for key,value in aqi_dataframes.items():
            value.to_excel(writer, sheet_name=key,index=False,header=True)
    with pd.ExcelWriter(WEATHER_DAILY_DATA_PATH) as writer:
        for key,value in weather_dataframes.items():
            value.to_excel(writer, sheet_name=key,index=False,header=True)

def train_lstm_model(data,parameter_type):
  model=LSTM_Model(50,1)
  model.load_data(data,parameter_type)
  model.execute()
  return model

def get_start_date(data):
  if "Date" in data.columns:
    data.drop('DATE',axis=1,inplace=True)
    data.rename(columns={'Date':'DATE'},inplace=True)
  start_date=data['DATE'].iloc[-1]+pd.Timedelta(days=1)
  return start_date

def get_forecasted_values(model,forecast_horizon,start_date):
  forecasted_values = model.forecast_future(15)
  df=create_dataframe(forecasted_values.reshape(1,15).tolist(),start_date,15,'D')
  return df
 
def get_daily_data(dir_path,city):
    aqi_city=[]
    weather_city=[]
    aqi_dir=dir_path+"/aqi"
    files = os.listdir(aqi_dir)
    for file in files:
        if os.path.isfile(os.path.join(aqi_dir, file)):
          path=os.path.join(aqi_dir, file)
          df=pd.read_excel(path,sheet_name=city,header=0)
          aqi_city.append(df)
    aqi_today=pd.concat(aqi_city)
    aqi_today=pd.DataFrame(aqi_today.mean()).T
    aqi_today['DATE']=pd.to_datetime(date.today(),format='%Y-%m-%d')
    aqi_today=aqi_today.dropna()
    weather_dir=dir_path+"/weather"
    files = os.listdir(weather_dir)
    for file in files:
        if os.path.isfile(os.path.join(weather_dir, file)):
          path=os.path.join(weather_dir, file)
          df=pd.read_excel(path,sheet_name=city,header=0)
          weather_city.append(df)
    weather_today=pd.concat(weather_city)
    weather_today=pd.DataFrame(weather_today.mean()).T
    weather_today['DATE']=pd.to_datetime(date.today(),format='%Y-%m-%d')
    weather_today=weather_today.dropna()
    return aqi_today,weather_today

    
if __name__=="__main__":
  try:
    print("\tDaily Scheduler")
    print("\t",datetime.datetime.now())
    for city in cities:
        print("******* City - {} ********".format(city))
        aqi_data,weather_data=get_weather_and_aqi_data(city)
        #Scrape New data from AQI DASHBOARD
        obj = ScrapeAqiWeather(URL_MAPPING[city], city)
        aqi_scrapped, weather_scrapped = get_daily_data('/home/ec2-user/scheduler/data/daily_scrapped',city)
        aqi_data['DATE']=pd.to_datetime(aqi_data['DATE'])
        #-----AQI-----
        #Append new AQI data to historical data
        if pd.to_datetime(aqi_scrapped['DATE'].iloc[-1]) in aqi_data['DATE'].values:
          aqi_data=aqi_data[:-1]
        aqi_data=aqi_data.append(aqi_scrapped,ignore_index=True)
        #Train model for AQI daily predictions and forecast
        aqi_model = train_lstm_model(aqi_data,"AQI")
        start_date_forecast=get_start_date(aqi_data)
        aqi_forecasted = get_forecasted_values(aqi_model,15,start_date_forecast)
        print("***** AQI Forecast********")
        # print(aqi_forecasted.head())
        # Upload the forecasted AQI csv to s3
        # upload_dataframe_to_s3(aqi_forecasted,'daily/aqi/{}/aqi-{}.csv'.format(city,str(date.today())))
        aqi_forecasted.to_csv('s3://capegemini-hackathon/daily/aqi/{}/aqi-{}.csv'.format(city,str(date.today())),index=False,header=True)
        #-------Weather--------

        #Append new Weather data to historical data
        if weather_scrapped['DATE'].iloc[-1] in weather_data['DATE'].values:
          weather_data=weather_data.iloc[:-1]
        
        weather_data=weather_data.append(weather_scrapped,ignore_index=True)
        # print(weather_data.tail(10))
        weather_data['DATE']=pd.to_datetime(weather_data['DATE'])
        #Train model for daily Weather predictions and forecast
        weather_model = train_lstm_model(weather_data,"Max Temp (°C)")
        start_date_forecast=get_start_date(weather_data)
        weather_forecasted = get_forecasted_values(weather_model,15,start_date_forecast)
        print("***** Weather Forecast********")
        print(weather_forecasted.head())
        # Upload the forecasted Weather csv to s3
        # upload_dataframe_to_s3(weather_forecasted,'daily/weather/{}/weather-{}.csv'.format(city,str(date.today())))
        weather_forecasted.to_csv('s3://capegemini-hackathon/daily/weather/{}/weather-{}.csv'.format(city,str(date.today())),index=False,header=True)
        #Store Updated Dataframes for each city
        aqi_dataframes[city]=aqi_data
        weather_dataframes[city]=weather_data
    #Upload Updated Daframes to s3    
    create_excel_files(aqi_dataframes,weather_dataframes)
  except Exception as e:
    print(e)