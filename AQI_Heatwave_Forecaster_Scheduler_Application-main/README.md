<div align="center">
<h1> AQI_Heatwave_Forecaster_Scheduler_Application
</h1>

<p>
The Scheduler Part of the application is a part of our add on feature to this application apart from the hacakthon's objective where we have planned to dynamically fetch the live data of AQI and Temperature from live data sources online by scrapping the websites and then training the model in a feeback basis by the scheduler application which run on our AWS EC2 instance.
</p>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
![Amazon AWS](https://img.shields.io/static/v1?style=for-the-badge&message=Amazon+AWS&color=232F3E&logo=Amazon+AWS&logoColor=FFFFFF&label=)

<hr>
</div>

## Scheduler's Used based on Time
1. Hourly Scheduler which runs every hour to Scrape the live data from the website
2. Hourly Scheduler which runs every hour to use the live data fetched from the scrapper to forecast the future values
3. Monthly Scheduler which runs every month to use the data generated for the month and forecast the future month's predictions 
---
## Architecture Diagram

![AQI architecture](https://user-images.githubusercontent.com/64360092/222782567-0fe00a6f-93fd-4563-b410-7fb086e536c5.png)

The above diagram shows the architecture of our entire application with including making dynamic predictions based on real time data using the scheduler application running on the AWS EC2 instance

---
## Hourly Scheduler for Scrapper
### Details
```
Scheduling Frequency : 15th minute of evry hour
Objective: To fetch live data and store it in EC2 local for dynamic redictions
```
### Idea and Implementation

  This scheduler run on the 15th minute of every hour and captures the live AQI and temperature values for the cities mentioned and stores them on to the EC2 local storage within the directory which will be used by the LSTM models in dynamically predicting the future values for the upcoming dates effectively. For to fetch the live data we written a web scrapping script using Beautiful Soup that fetches the live data from the [AQI Dashboard Website](https://www.aqi.in/in/dashboard/india/telangana).
  
---
## Hourly Scheduler for Dynamic Daily Data Future Forecasing
### Details
```
Scheduling Frequency : 30th minute of evry hour
Objective: To fetch the live data that is stored by the scrapper application and considering the past daily data to forecast the future values for the next 15 days.
```
### Idea and Implementation

  This scheduler run on the 30th minute of every hour and uses the the historical data before today and average of the scrapper application's data generated and stored on local until the current hour to train the LSTM model on this data and forecast the values for the next 15 days. The forecasted values are stored on to S3 bucket by the scheduler scipt itself which will be fetched by the backend application and te forecasted values are displayed onto the website
  
---
## Monthly Scheduler for Dynamic Monhtly Data Future Forecasing
### Details
```
Scheduling Frequency : 1st day of every month
Objective: To fetch the live daily dataof the month that is stored in s3 by the daily scrapper application and considering the past monthly data to forecast the future values for the next 15 monhts.
```
### Idea and Implementation

  This scheduler run on the 1st day of every month and uses the the historical monhtly data before the last month and average of the scrapper application's data generated daily for the previous month stored on S3 Bucket the current day to train the LSTM model on this data and forecast the values for the next 15 months. This feature aloows us to forecast the future predictions aon a monthly basis taking into consideration the current values as well. The forecasted values are stored on to S3 bucket by the scheduler scipt itself which will be fetched by the backend application and te forecasted values are displayed onto the website.
  
 ---
*Thus from an application point of view in the notion of extending this to a starup application in supporting the environment we have build this application as a scalable application by taking into account the live data in making future predicts as an add on feature, which would make the predictions still more reliable and accurate*
