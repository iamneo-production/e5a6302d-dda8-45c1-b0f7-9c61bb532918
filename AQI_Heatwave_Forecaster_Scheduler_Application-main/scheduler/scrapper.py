from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import Request, urlopen
from datetime import date

class ScrapeAqiWeather():
    def __init__(self, url, city_name):
        """initialize the values

        Args:
            url (STRING)
            city_name (STRING)
        """
        self.url = url
        self.city_name = city_name
        self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                        'Accept-Encoding': 'none',
                        'Accept-Language': 'en-US,en;q=0.8',
                        'Connection': 'keep-alive'}
        self.aqi_data = {}
        self.weather_data = {}

    def get_aqi_data(self, soup):
        """parses the html page

        Args:
            soup (BeautifulSoup object): url_page

        Returns:
            Tuple of required dictionary 
        """
        pollutants = {}
        aqi_pollutants = soup.find_all(
            'div', {"class": "card-Pollutants-sensor"})
        for val in aqi_pollutants:
            name = val.find(
                'span', {"class": "Pollutants_sensor_text_s"}).get_text().strip()
            name = name.replace("(", '')
            name = name.replace(")", '')
            value = val.find(
                'span', {"class": "Pollutants_sensor_text"}).get_text().strip()
            value = value.replace(",", '')
            pollutants[name] = int(value)

        weather = {}
        aqi_val = soup.find('table', {"id": "state-table"})
        table_col, table_data = aqi_val.find('thead'),  aqi_val.find('tbody')
        table_data = table_data.find_all('td')
        table_col = table_col.find_all('th')[1:]
        for val in zip(table_col, table_data):
            name, value = val
            name, value = name.get_text().strip(), value.get_text().strip()
            value = value.replace(",", '')
            if name == 'AQI-IN':
                pollutants['AQI'] = int(value)
            elif name == 'Temp':
                weather['Max Temp (°C)'] = float(value)
            elif name == 'Humid':
                weather['Max Humidity (%)'] = float(value)

        wind_speed = soup.find(
            'div', {"class": "weather-all-data-wind d-flex"})
        wind_speed = wind_speed.find(
            'p', {"class": "card-cloudy-text-wind"}).get_text().strip()
        wind_speed = wind_speed.split(" ")[0]
        weather['Max Wind Speed (Kmph)'] = float(wind_speed)

        return pollutants, weather

    def prepare_dict_for_csv(self):
        """prepares the dictionary for csv file
        """
        del self.aqi_data['CO']
        del self.aqi_data['Ozone']
        self.aqi_data['NH3'] = 0

        self.weather_data['Min Temp (°C)'] = float(0)
        self.weather_data['Min Humidity (%)'] = float(0)
        self.weather_data['Rain (mm)'] = float(0)
        self.weather_data['District'] = self.city_name.title()

    def scrape_from_url(self):
        """scrape the given webpage store it in a csv file

        Returns:
            Tuple of required Data frame(optional)
        """
        req = Request(self.url, headers=self.headers)
        html_page = urlopen(req)

        soup = BeautifulSoup(html_page, "html.parser")

        self.aqi_data, self.weather_data = self.get_aqi_data(soup)
        today = date.today()
        self.aqi_data['DATE'], self.weather_data['Date'] = today, today
        self.prepare_dict_for_csv()

        aqi_df = pd.DataFrame([self.aqi_data])
        weather_df = pd.DataFrame([self.weather_data])

        # aqi_df.to_csv('aqi-{}-{}.csv'.format(self.city_name,
        #               today), header=True, index=False)
        # weather_df.to_csv(
        #     'weather-{}-{}.csv'.format(self.city_name, today), header=True, index=False)

        return aqi_df, weather_df
