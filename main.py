import requests
from getweather import RealWeather

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.8/onecall"
API_KEY = "be6b819e6631efa5f3b04ec84da3d06a"

rw = RealWeather()
meteo_current_temp = rw.get_current_temp()

places = {
    "SGGW":  (52.160382, 21.053312)
}
weather_raport = ""

for city, location in places.items():
    parameters = {
        "lat": location[0],
        "lon": location[1],
        "appid": API_KEY,
        "exclude": "minutely,hourly,daily,alerts",
    }

    response = requests.get(url=OWM_ENDPOINT, params=parameters)
    response.raise_for_status()
    weather_data = response.json()

    omw_current_temp = round(float(weather_data["current"]["temp"]) - 273.15, 1)
    print(omw_current_temp)
    weather_raport += f"{city} -> OMW: {omw_current_temp}, Meteo: {meteo_current_temp}\n"

with open(file="data/raport.txt", mode="a", encoding="UTF-8") as raport:
    raport.write(weather_raport)
