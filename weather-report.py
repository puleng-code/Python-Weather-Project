import json, requests, datetime
from time import ctime
from datetime import date

# Gives us access to the data
api_key = "829a6b73087473ad6247a51bb6850ab5"
# URL that will provide us with data
base_url = "http://api.openweathermap.org/data/2.5/weather?"

cdate = date.today()
date_t = cdate.strftime("%Y %B %d")

c_time = datetime.datetime.now()

report = input("Generate weather report? (Y/N): ")

if report.upper() == 'Y':
  print("\n")
  print("Date: ", date_t,"     ", c_time.strftime("%H:%M:%S"))

  cities = ["Cape Town","Bloemfontein","Johannesburg","Pretoria"]
  for city in cities:
    city_name = city
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    api_response = requests.get(complete_url)
    response = api_response.json()
    
    print(city_name,":","Wind:", response["wind"]["speed"],",", "max temp:",
    response["main"]["temp_max"],",", "min temp", response["main"]["temp_min"])
       
elif report.upper() == 'N':
    exit()




