<div align="center">
<h1> Backend for AQI-Heatwave-Forecaster
</h1>

<p>
Basic Flask application to make model prediction of AQI and Heatwaves for the Tier-2 cites in Telangana with various endpoints as mentioned below.
</p>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
![Flask](https://img.shields.io/static/v1?style=for-the-badge&message=Flask&color=000000&logo=Flask&logoColor=FFFFFF&label=)
![Amazon AWS](https://img.shields.io/static/v1?style=for-the-badge&message=Amazon+AWS&color=232F3E&logo=Amazon+AWS&logoColor=FFFFFF&label=)

<hr>
</div>


## Setting Up Application

1. Create and Activate the virtual env
```
    python3 -m venv venv
    venv\Scripts\activate.bat
```

2. Install the required python packages
```
    pip3 install -r requirements.txt
```

3. Run the Application

```
set FLASK_APP=index.py
set FLASK_ENV=development
flask run
```


## Sample request to our flask application

![Screen Recording - 3 March 2023 (1)](https://user-images.githubusercontent.com/62760269/222525992-b5b129df-dcb3-4315-b7b7-17ef88bdb451.gif)




**API-Endpoints**
----

* **URL**

  https://aqi-heatwave-app.azurewebsites.net/api/aqi/getMonthlyAQIPredictions
  
* **Description** 

  Returns the monthly AQI Predictions of the given city for the next 15 months

* **Method:**

  `POST`  
  
*  **URL Params**
   
   None
   
* **Data Params**
   
   ```

    {
        
        "City":"city_name"
      
    }
    ```

* **Success Response:**
  
  * **Code:** 200 <br />
    **Content:** 
    ```json
    [
      {
        "Date": "2023-03-01",
        "Predictions": 86.5634307861
      },
      {
        "Date": "2023-04-01",
        "Predictions": 75.4241104126
      },
      {
        "Date": "2023-05-01",
        "Predictions": 70.9274902344
      },
      {
        "Date": "2023-06-01",
        "Predictions": 69.1306838989
      },
      {
        "Date": "2023-07-01",
        "Predictions": 68.4158325195
      },
      {
        "Date": "2023-08-01",
        "Predictions": 68.1319503784
      },
      {
        "Date": "2023-09-01",
        "Predictions": 68.01927948
      },
      {
        "Date": "2023-10-01",
        "Predictions": 67.9745864868
      },
      {
        "Date": "2023-11-01",
        "Predictions": 67.9568557739
      },
      {
        "Date": "2023-12-01",
        "Predictions": 67.9498214722
      },
      {
        "Date": "2024-01-01",
        "Predictions": 67.9470291138
      },
      {
        "Date": "2024-02-01",
        "Predictions": 67.945930481
      },
      {
        "Date": "2024-03-01",
        "Predictions": 67.9454879761
      },
      {
        "Date": "2024-04-01",
        "Predictions": 67.9453125
      },
      {
        "Date": "2024-05-01",
        "Predictions": 67.9452514648
      }
    ]

    ```



* **URL**

  https://aqi-heatwave-app.azurewebsites.net/api/aqi/getDailyAQIPredictions
  
* **Description**

  Returns the daily AQI predictions of the given city for the next 15 days


* **Method:**

  `POST`  
  
*  **URL Params**

   None
   
* **Data Params**
  
  ```

    {
       
       "City":"city_name"
      
    }
    ```

* **Success Response:**
  
  * **Code:** 200 <br />
    **Content:** 
    ```json
    [
      {
        "Date": "2023-03-03",
        "Predictions": 152.5825500488
      },
      {
        "Date": "2023-03-04",
        "Predictions": 139.2323303223
      },
      {
        "Date": "2023-03-05",
        "Predictions": 134.1151885986
      },
      {
        "Date": "2023-03-06",
        "Predictions": 132.167678833
      },
      {
        "Date": "2023-03-07",
        "Predictions": 131.4286193848
      },
      {
        "Date": "2023-03-08",
        "Predictions": 131.1484375
      },
      {
        "Date": "2023-03-09",
        "Predictions": 131.0422821045
      },
      {
        "Date": "2023-03-10",
        "Predictions": 131.0020751953
      },
      {
        "Date": "2023-03-11",
        "Predictions": 130.9868469238
      },
      {
        "Date": "2023-03-12",
        "Predictions": 130.9810638428
      },
      {
        "Date": "2023-03-13",
        "Predictions": 130.9788818359
      },
      {
        "Date": "2023-03-14",
        "Predictions": 130.9780578613
      },
      {
        "Date": "2023-03-15",
        "Predictions": 130.9777374268
      },
      {
        "Date": "2023-03-16",
        "Predictions": 130.9776153564
      },
      {
        "Date": "2023-03-17",
        "Predictions": 130.9775848389
      }
    ]
    ```
    
    
    
    
* **URL**

  https://aqi-heatwave-app.azurewebsites.net/api/aqi/getHistoryMonthlyAQI\
 
* **Description**

  Return the Monthly AQI historical Data which is used for model training

* **Method:**

  `POST`  
  
*  **URL Params**

   None
   
* **Data Params**
  
  ```

    {
        
        "City":"city_name"
      
    }
    ```

* **Success Response:**
  
  * **Code:** 200 <br />
    **Content:** 
    ```json
    [
      {
        "DATE": "2016-01-01T00:00:00.000Z",
        "SO2": 5.89,
        "NO2": 23.17,
        "PM10": 62,
        "PM2.5": 36.45,
        "NH3": 15.65,
        "AQI": 67.33333333
      },
      {
        "DATE": "2016-02-01T00:00:00.000Z",
        "SO2": 5.89,
        "NO2": 23.17,
        "PM10": 68,
        "PM2.5": 36.45,
        "NH3": 15.65,
        "AQI": 68.33333333
      },
      {
        "DATE": "2016-03-01T00:00:00.000Z",
        "SO2": 5.89,
        "NO2": 23.17,
        "PM10": 71,
        "PM2.5": 36.45,
        "NH3": 15.65,
        "AQI": 71.11111111
      },
      {
        "DATE": "2016-04-01T00:00:00.000Z",
        "SO2": 5.89,
        "NO2": 23.17,
        "PM10": 70,
        "PM2.5": 36.45,
        "NH3": 15.65,
        "AQI": 69.55555556
      },
      {
        "DATE": "2016-05-01T00:00:00.000Z",
        "SO2": 5.89,
        "NO2": 23.17,
        "PM10": 69,
        "PM2.5": 40,
        "NH3": 15.65,
        "AQI": 70.55555556
      },
      {
        "DATE": "2016-06-01T00:00:00.000Z",
        "SO2": 4,
        "NO2": 15,
        "PM10": 66,
        "PM2.5": 40,
        "NH3": 21,
        "AQI": 40.11111111
      },
      {
        "DATE": "2016-07-01T00:00:00.000Z",
        "SO2": 4,
        "NO2": 16,
        "PM10": 60,
        "PM2.5": 30,
        "NH3": 21,
        "AQI": 59.88888889
      }
    ]
    ```
    
    
    
        
* **URL**

  https://aqi-heatwave-app.azurewebsites.net/api/aqi/getHistoryDailyAQI
  
* **Description**

  Returns the Daily AQI historical Data which is used for model training

* **Method:**

  `POST`  
  
*  **URL Params**

   None
   
* **Data Params**
  
  ```

    {
        "City":"city_name"
    }
    ```

* **Success Response:**
  
  * **Code:** 200 <br />
    **Content:** 
    ```json
    [
      {
        "DATE": "2023-01-27T00:00:00.000Z",
        "AQI": 126.5,
        "PM2.5": 67.5,
        "PM10": 121.5,
        "SO2": 4.5,
        "NO2": 14.5,
        "NH3": 0
      },
      {
        "DATE": "2023-01-28T00:00:00.000Z",
        "AQI": 159,
        "PM2.5": 77.5,
        "PM10": 134.5,
        "SO2": 3.5,
        "NO2": 12.5,
        "NH3": 0
      },
      {
        "DATE": "2023-01-29T00:00:00.000Z",
        "AQI": 180,
        "PM2.5": 84,
        "PM10": 155.5,
        "SO2": 3,
        "NO2": 14,
        "NH3": 0
      },
      {
        "DATE": "2023-01-30T00:00:00.000Z",
        "AQI": 197.5,
        "PM2.5": 89.5,
        "PM10": 144.5,
        "SO2": 2.5,
        "NO2": 14.5,
        "NH3": 0
      },
      {
        "DATE": "2023-01-31T00:00:00.000Z",
        "AQI": 202,
        "PM2.5": 90.5,
        "PM10": 150,
        "SO2": 6,
        "NO2": 11.5,
        "NH3": 0
      },
      {
        "DATE": "2023-02-01T00:00:00.000Z",
        "AQI": 102,
        "PM2.5": 52,
        "PM10": 90,
        "SO2": 6.5,
        "NO2": 10,
        "NH3": 0
      },
      {
        "DATE": "2023-02-02T00:00:00.000Z",
        "AQI": 73.5,
        "PM2.5": 32.5,
        "PM10": 74,
        "SO2": 5.5,
        "NO2": 12.5,
        "NH3": 0
      },
      {
        "DATE": "2023-02-03T00:00:00.000Z",
        "AQI": 77.5,
        "PM2.5": 41.5,
        "PM10": 78.5,
        "SO2": 4.5,
        "NO2": 13.5,
        "NH3": 0
      }
    ]
    ```
    
    
    
        
* **URL**

  https://aqi-heatwave-app.azurewebsites.net/api/weather/getMonthlyWeatherPredictions
 
* **Description**

  Returns the Monthly Temperature predictions of the given city for the next 15 months
 

* **Method:**

  `POST`  
  
*  **URL Params**

   None
   
* **Data Params**
  
  ```

    {
        "City":"city_name"
    }
    ```

* **Success Response:**
  
  * **Code:** 200 <br />
    **Content:** 
    ```json
    [
      {
        "Unnamed: 0": 0,
        "Date": "2023-03-01",
        "Predictions": 36.694229126
      },
      {
        "Unnamed:0": 1,
        "Date": "2023-04-01",
        "Predictions": 37.8973579407
      },
      {
        "Unnamed:0": 2,
        "Date": "2023-05-01",
        "Predictions": 38.501953125
      },
      {
        "Unnamed:0": 3,
        "Date": "2023-06-01",
        "Predictions": 38.810295105
      },
      {
        "Unnamed:0": 4,
        "Date": "2023-07-01",
        "Predictions": 38.9686889648
      },
      {
        "Unnamed:0": 5,
        "Date": "2023-08-01",
        "Predictions": 39.0503501892
      },
      {
        "Unnamed:0": 6,
        "Date": "2023-09-01",
        "Predictions": 39.0925292969
      },
      {
        "Unnamed:0": 7,
        "Date": "2023-10-01",
        "Predictions": 39.1143379211
      },
      {
        "Unnamed:0": 8,
        "Date": "2023-11-01",
        "Predictions": 39.125617981
      },
      {
        "Unnamed:0": 9,
        "Date": "2023-12-01",
        "Predictions": 39.1314544678
      },
      {
        "Unnamed:0": 10,
        "Date": "2024-01-01",
        "Predictions": 39.134475708
      },
      {
        "Unnamed:0": 11,
        "Date": "2024-02-01",
        "Predictions": 39.1360359192
      },
      {
        "Unnamed:0": 12,
        "Date": "2024-03-01",
        "Predictions": 39.136844635
      },
      {
        "Unnamed:0": 13,
        "Date": "2024-04-01",
        "Predictions": 39.137260437
      },
      {
        "Unnamed:0": 14,
        "Date": "2024-05-01",
        "Predictions": 39.1374778748
      }
    ]
    ```
    
    
            
* **URL**

  https://aqi-heatwave-app.azurewebsites.net/api/weather/getDailyWeatherPredictions
  
* **Description**

  Returns the Daily Temperature predictions for the next 15 days

* **Method:**

  `POST`  
  
*  **URL Params**

   None
   
* **Data Params**
  
  ```

    {
        "City":"city_name"
    }
    ```

* **Success Response:**
  
  * **Code:** 200 <br />
    **Content:** 
    ```json
    [
      {
        "Date": "2023-03-03",
        "Predictions": 30.9923744202
      },
      {
        "Date": "2023-03-04",
        "Predictions": 31.6077327728
      },
      {
        "Date": "2023-03-05",
        "Predictions": 32.1008071899
      },
      {
        "Date": "2023-03-06",
        "Predictions": 32.5022888184
      },
      {
        "Date": "2023-03-07",
        "Predictions": 32.8333625793
      },
      {
        "Date": "2023-03-08",
        "Predictions": 33.1091842651
      },
      {
        "Date": "2023-03-09",
        "Predictions": 33.3409042358
      },
      {
        "Date": "2023-03-10",
        "Predictions": 33.5369262695
      },
      {
        "Date": "2023-03-11",
        "Predictions": 33.7037086487
      },
      {
        "Date": "2023-03-12",
        "Predictions": 33.8463020325
      },
      {
        "Date": "2023-03-13",
        "Predictions": 33.9687271118
      },
      {
        "Date": "2023-03-14",
        "Predictions": 34.0741958618
      },
      {
        "Date": "2023-03-15",
        "Predictions": 34.1653366089
      },
      {
        "Date": "2023-03-16",
        "Predictions": 34.2442893982
      },
      {
        "Date": "2023-03-17",
        "Predictions": 34.3128433228
      }
    ]

    ```
    
      
            
* **URL**

  https://aqi-heatwave-app.azurewebsites.net/api/weather/getHistoryMonthlyWeather
  
  
 * **Description**

  Return the Monthly Temperature historical Data which is used for model training

* **Method:**

  `POST`  
  
*  **URL Params**

   None
   
* **Data Params**
  
  ```

    {
        "City":"city_name"
    }
    ```

* **Success Response:**
  
  * **Code:** 200 <br />
    **Content:** 
    ```json
    [
      {
        "Date": "2018-01",
        "Max Temp": 35.8,
        "Rain (mm)": 0,
        "Min Temp": 21,
        "Min Humidity": 45.2,
        "Max Humidity": 99.9,
        "Min WindSpeed": 4.6,
        "Max Wind Speed": 24.7
      },
      {
        "Date": "2018-02",
        "Max Temp": 38.8,
        "Rain (mm)": 36.3,
        "Min Temp": 24.4,
        "MinHumidity": 59.3,
        "Max Humidity": 100,
        "Min Wind Speed": 6.1,
        "Max Wind Speed": 48.3
      },
      {
        "Date": "2018-03",
        "Max Temp": 41.9,
        "Rain(mm)": 10,
        "Min Temp": 27.6,
        "Min Humidity": 70.9,
        "Max Humidity": 100,
        "Min Wind Speed": 3.9,
        "Max WindSpeed": 52.6
      },
      {
        "Date": "2018-04",
        "Max Temp": 44.3,
        "Rain (mm)": 18.5,
        "Min Temp": 31.9,
        "Min Humidity": 49.1,
        "MaxHumidity": 100,
        "Min Wind Speed": 6,
        "Max Wind Speed": 59
      },
      {
        "Date": "2018-05",
        "Max Temp": 45.1,
        "Rain (mm)": 45.8,
        "MinTemp": 33.8,
        "Min Humidity": 57.6,
        "Max Humidity": 99.9,
        "Min Wind Speed": 11,
        "Max Wind Speed": 64.4
      },
      {
        "Date": "2018-06",
        "MaxTemp": 42.5,
        "Rain (mm)": 128.8,
        "Min Temp": 29.9,
        "Min Humidity": 82.3,
        "Max Humidity": 100,
        "Min Wind Speed": 14.2,
        "Max Wind Speed": 57.6
      }
    ]
    ``` 
    
          
            
* **URL**

  https://aqi-heatwave-app.azurewebsites.net/api/weather/getHistoryDailyWeather
  
  
* **Description**

  Return the Daily Temperature historical Data which is used for model training

* **Method:**

  `POST`  
  
*  **URL Params**

   None
   
* **Data Params**
  
  ```

    {
        "City":"city_name"
    }
    ```

* **Success Response:**
  
  * **Code:** 200 <br />
    **Content:** 
    ```json
      [
    {
      "DATE": "2018-01-01T00:00:00.000Z",
      "Max Temp": 33.5,
      "Rain (mm)": 0,
      "Min Temp": 16.8,
      "Min Humidity": 41.8,
      "MaxHumidity": 88.1,
      "Min Wind Speed": 2,
      "MaxWindSpeed": 19.7
    },
    {
      "DATE": "2018-01-02T00:00:00.000Z",
      "Max Temp": 33.2,
      "Rain(mm)": 0,
      "Min Temp": 16.9,
      "Min Humidity": 38.8,
      "Max Humidity": 85,
      "Min Wind Speed": 3,
      "Max WindSpeed": 17.6
    },
    {
      "DATE": "2018-01-03T00:00:00.000Z",
      "Max Temp": 32.7,
      "Rain (mm)": 0,
      "Min Temp": 14.7,
      "Min Humidity": 41.6,
      "MaxHumidity": 85.1,
      "Min Wind Speed": 1.2,
      "Max Wind   Speed": 18.8
    },
    {
      "DATE": "2018-01-04T00:00:00.000Z",
      "Max Temp": 32.2,
      "Rain (mm)": 0,
      "Min Temp": 14.9,
      "Min Humidity": 42.1,
      "Max Humidity": 86.8,
      "Min Wind Speed": 0.8,
      "Max WindSpeed": 16.4
    },
    {
      "DATE": "2018-01-05T00:00:00.000Z",
      "Max Temp": 32.4,
      "Rain (mm)": 0,
      "Min Temp": 14.3,
      "Min Humidity": 40.9,
      "Max Humidity": 86.5,
      "Min Wind Speed": 0,
      "Max Wind Speed": 19.2
    },
    {
      "DATE": "2018-01-06T00:00:00.000Z",
      "Max Temp": 34.9,
      "Rain(mm)": 0,
      "Min Temp": 16,
      "Min Humidity": 38.2,
      "Max Humidity": 83.4,
      "Min Wind Speed": 3.4,
      "Max WindSpeed": 20.9
    }
    ]
    ``` 
    
    
    
    

 

