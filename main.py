import requests
from getweather import RealWeather

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.8/onecall"
API_KEY = "be6b819e6631efa5f3b04ec84da3d06a"

rw = RealWeather()
meteo_current_temp = rw.get_current_temp()

places = {
    # "Warszawa": (52.160194261987144, 21.05261494179747),
    # "Szczecin": (53.42753724328469, 14.54908158815107),
    # "Wrocław": (51.107565888640025, 17.037857576578876),
    # "Białystok": (53.191964476549664, 23.11579556156424),
    # "Rzeszów": (50.07149541312731, 21.99282456479467),
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
    weather_raport += f"{city} -> OMW: {omw_current_temp}, Real: {meteo_current_temp}\n"

with open(file="data/raport.txt", mode="a", encoding="UTF-8") as raport:
    raport.write(weather_raport)
