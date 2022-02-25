# DSC 510
# Week 12
# 12.1 Final Project Programming Assignment
# Author Prashant Raghuwanshi
# Date Created: 06-02-2021
# Program Description: 12.1 ->  This program takes zipcode or city name input from user and provides
# the corresponding entered location weather forecast information to user
#===================================================================================================##
import requests
from datetime import datetime
import pandas as pd
import stringcase
from urllib3.exceptions import HTTPError as BaseHTTPError


class fetchweather:

    def __init__(self, APIKEY, weatherurl, zipurl):
        self.APIKEY = APIKEY
        self.weatherurl = weatherurl
        self.zipurl = zipurl

    def fetchcurweatherbycity(self, uscity):
        countrycode = 'us'
        req_weather = makecall(self.weatherurl, 'weather?q='+uscity+','+countrycode+'&APPID='+self.APIKEY+'&units=imperial')
        data = req_weather.json()
        printcity = (data['name'])
        categorydict=data["main"]
        print(f'----------------------------------------')
        print(f'Current Weather Report for {printcity} City')
        print(f'Current DATE & Time= {datetime.now()}')
        print(f'----------------------------------------')
        print(f'Weather Parameters :  Value')
        print(f'----------------------------------------')
        for key, value in categorydict.items():
            print("{:<18} {:<4}".format(key, value))

    def fetchcurweatherbyzip(self, uszip):
        countrycode = 'us'
        req_weather = makecall(self.weatherurl, 'weather?zip='+uszip+','+countrycode+'&APPID='+self.APIKEY+'&units=imperial')
        data = req_weather.json()
        printcity = (data['name'])
        categorydict=data["main"]
        print(f'----------------------------------------')
        print(f'Current Weather Report for {printcity} City')
        print(f'Current DATE & Time= {datetime.now()}')
        print(f'----------------------------------------')
        print(f'Weather Parameters :  Value')
        print(f'----------------------------------------')
        for key, value in categorydict.items():
            print("{:<18} {:<4}".format(key, value))

    def fetchfurweatherbycity(self, uscity):
        countrycode = 'us'
        freq_weather = makecall(self.weatherurl, 'forecast?q='+uscity+','+countrycode+'&APPID='+self.APIKEY+'&units=imperial&cnt=3')
        fdata = freq_weather.json()
        for nested_list in fdata["list"]:
            categorydict = nested_list["main"]
            forecastdate=nested_list["dt_txt"]
            print(f'----------------------------------------')
            print(f'FORCASTED Weather Report FOR {uscity} City')
            print(f'FORCAST DATE & Time= {forecastdate}')
            print(f'----------------------------------------')
            print(f'Weather Parameters :  Value')
            print(f'----------------------------------------')
            for key, value in categorydict.items():
                print("{:<20} {:<4}".format(key, value))
        print(f'----FORECAST REPORTS ENDS---------------')

    def fetchfurweatherbyzip(self, uszip):
        countrycode = 'us'
        freq_weather = makecall(self.weatherurl, 'forecast?zip='+uszip+','+countrycode+'&APPID='+self.APIKEY+'&units=imperial&cnt=3')
        fdata = freq_weather.json()
        uscity=(fdata['city']['name'])
        for nested_list in fdata["list"]:
            categorydict = nested_list["main"]
            forecastdate=nested_list["dt_txt"]
            print(f'----------------------------------------')
            print(f'FORCASTED Weather Report FOR {uscity} City')
            print(f'FORCAST DATE & Time= {forecastdate}')
            print(f'----------------------------------------')
            print(f'Weather Parameters :  Value')
            print(f'----------------------------------------')
            for key, value in categorydict.items():
                print("{:<20} {:<4}".format(key, value))
            print(f'----FORECAST REPORTS ENDS---------------')

    def process(self):
            lkpweatherby = input("Would you like to lookup weather data by US City or zip code ? "
                         "Enter 1 for US City 2 for zip:")
            try:
                if (isinstance(int(lkpweatherby), int) == True):
                    lkpweatherby = int(lkpweatherby)
            except:
                lkpweatherby = int(input('input selection code is not valid , please reenter the valid code:'))
            if lkpweatherby == 1:
                uscity = input('Enter the City name:')
                statecode = input('Enter State code:')
                statedata = self.validate_city_state(uscity, statecode)
                if statedata[1] == 1:
                    self.fetchcurweatherbycity(uscity)
                    self.fetchfurweatherbycity(uscity)
                else:
                    uscity = input('Re-Enter the City name:')
                    statecode = input('Re-Enter State code:')
                    statedata = self.validate_city_state(uscity, statecode)
                    if statedata[1] == 1:
                        self.fetchcurweatherbycity(statedata[0])
                        self.fetchfurweatherbycity(statedata[0])
                    else:
                        print('Input State or City name is not valid, Moving control back to Forcast Terminal')
            elif lkpweatherby == 2:
                uszip = input('Enter usa zipcode :')
                zipdata = self.validate_zipcode(uszip)
                if ('Error' in zipdata.keys()) or len(zipdata) == 0:
                    if len(zipdata) == 0:
                        print(f'Entered Zipcode={uszip} is Not found in our Database')
                    else:
                        print(f'Entered Zipcode={uszip} is not valid: {zipdata}')
                    uszip = input('Re-Enter valid usa zipcode :')
                    zipdata = self.validate_zipcode(uszip)
                    if ('Error' in zipdata.keys()) or len(zipdata) == 0:
                        print('invalid Zipcode, Moving control back to Forcast Terminal')
                    else:
                        self.fetchcurweatherbyzip(uszip)
                        self.fetchfurweatherbyzip(uszip)
                else:
                    self.fetchcurweatherbyzip(uszip)
                    self.fetchfurweatherbyzip(uszip)
            else:
                print(' invalid option selected')

    def validate_city_state(self, cityname, statecode):
        city_name = stringcase.titlecase(cityname)
        state_code = stringcase.uppercase(statecode)
        validind = 0
        # Get the city list from OpenWeatherMap, read to pandas dataframe
        url = 'http://bulk.openweathermap.org/sample/city.list.json.gz'
        df = pd.read_json(url)
        # Search dataframe for city_name, state_code combination
        # df['country'] == 'US' - ONLY US CITIES IN SCOPE FOR FINAL PROJECT
        location_query = df.loc[(df['name'] == city_name) & (df['state'] == state_code) & (df['country'] == 'US'),
                               ['id', 'name', 'state', 'country', 'coord']]

        # If only one exists, set lat longs and city name, city, and/or state_code or any combo of them
        if len(location_query) == 1:
            # Get values from pandas series of results
            longitude = location_query.coord.str['lon'].iloc[0]
            latitude = location_query.coord.str['lat'].iloc[0]
            city = str(location_query['name'].iloc[0]).strip()
            state_code = str(location_query['state'].iloc[0]).strip()
            city_state = (city + ', ' + state_code)
            # If none exist
            validind = 1
        else:
            print(f'Invalid Entry for City = {city_name} or State code = {state_code}')
            validind = 0
        if validind ==0:
            return 'BAD ENTRY', validind
        else:
            return city_state, validind

    def validate_zipcode(self, zipcode):
        # Get the city list from OpenWeatherMap, read to pandas dataframe
        val_zip = makecall(self.zipurl, zipcode+'?key=')
        zipdata = val_zip.json()
        return zipdata


def makecall(url, mpath):
    try:
      getdata = ''
      getdata = requests.get(url+mpath)
      print()
      return getdata
    except requests.exceptions.IOError as ioerr:
        print("IOError", ioerr.response.text)

    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh.response.text)

    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc.response.text)

    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt.response.text)

    except requests.exceptions.RequestException as err:
        print("OOps: Something Else", err.response.text)


def main():
   try:
        print(f'Hello User ,Welcome to Weather Forecast Display System: ')
        weatherurl = 'http://api.openweathermap.org/data/2.5/'
        zipurl = 'https://api.zip-codes.com/ZipCodesAPI.svc/1.0/QuickGetZipCodeDetails/'
        weatherurlapikey = ''
        continueoperation = 'Y'
        weatherinstance = fetchweather(weatherurlapikey, weatherurl, zipurl)
        while continueoperation == 'Y' or continueoperation == 'y':
            weatherinstance.process()
            print('Enter Y or y if you want to continue with weather forcast else press any key to exit from terminal')
            continueoperation = input()
        exit(100)
   except:
       print('Exiting out from Terminal')

if __name__ == '__main__':
    main()
