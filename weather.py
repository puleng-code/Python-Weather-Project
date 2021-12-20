import json, requests
from requests.models import cookiejar_from_dict
# Gives us access to the data
api_key = "829a6b73087473ad6247a51bb6850ab5"
# URL that will provide us with data
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# City we will fetch data for
city_name = input("Input a city: ")
 
# Stores complete url address
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

# uses requests package to fetch data at that url
api_response = requests.get(complete_url)
# Puts the data in a readable format
response = api_response.json()
# print the data we receive
weather = response["weather"]
dict = weather[0]
dict["description"]
def retrieve_weather_data_for_city(city_name):
    print(city_name)
    print(base_url)

def convert_kelvin_to_celsius(temperature):
    new_temp = int(temperature - 273.15)
    return new_temp

convert_kelvin_to_celsius(response["main"]["temp"])

print(response)
print(complete_url)
#[city name]|temp in (Kelvin)|temp [humidity]|[description]
print("City: ", city_name,"|", "Temperature ",convert_kelvin_to_celsius(response["main"]["temp"]),"℃","|","Humidity ",
response["main"]["humidity"],"|", response["weather"][0]["description"])
