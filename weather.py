from bs4 import BeautifulSoup
import requests


METEO_ENDPOINT = "https://sggw.meteo.waw.pl/"
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.8/onecall"
API_KEY = "be6b819e6631efa5f3b04ec84da3d06a"
COORDINATES = (52.160382, 21.053312)


class Meteo:
    """Class responsible for getting meteo current weather."""

    def __init__(self):
        """Requests webpage source 'html' and creates Beautiful Soup."""
        # Request webpage source.
        response = requests.get(url=METEO_ENDPOINT)
        response.raise_for_status()
        meteo_web_page = response.text

        # Create soup object.
        self.soup = BeautifulSoup(meteo_web_page, "html.parser")

    def get_current_weather(self):
        """Returns Meteos current temperature."""
        # weather = {
        #     "temperature": float(self.soup.select_one("div.left:nth-child(3) > div:nth-child(1)").getText().split()[1].replace(",", ".")),
        #     "feels_like": float(self.soup.select_one("table.tab_msrs1:nth-child(5)").getText().split()[5].replace(",", ".").replace("odczuwalna", "")),
        #     "humidity": int(float(self.soup.select_one("div.left:nth-child(4) > div:nth-child(1)").getText().split()[1].replace(",", "."))),
        #     "dew_point": float(self.soup.select_one("table.tab_msrs1:nth-child(5)").getText().split()[2].replace(",", ".").replace("rosy", "")),
        #     "wind_speed": float(self.soup.select_one("div.plotbox:nth-child(1) > div:nth-child(1)").getText().split()[1].replace(",", ".")),
        #     "wind_direction": int(float(self.soup.select_one("div.left:nth-child(2) > div:nth-child(1)").getText().split()[1].replace(",", ".")))
        # }
        weather = [
            float(self.soup.select_one("div.left:nth-child(3) > div:nth-child(1)").getText().split()[1].replace(",", ".")),
            float(self.soup.select_one("table.tab_msrs1:nth-child(5)").getText().split()[5].replace(",", ".").replace("odczuwalna", "")),
            int(float(self.soup.select_one("div.left:nth-child(4) > div:nth-child(1)").getText().split()[1].replace(",", "."))),
            float(self.soup.select_one("table.tab_msrs1:nth-child(5)").getText().split()[2].replace(",", ".").replace("rosy", "")),
            float(self.soup.select_one("div.plotbox:nth-child(1) > div:nth-child(1)").getText().split()[1].replace(",", ".")),
            int(float(self.soup.select_one("div.left:nth-child(2) > div:nth-child(1)").getText().split()[1].replace(",", ".")))
        ]
        return weather


class OWM:
    """Class responsible for getting OMW current weather."""

    def __init__(self):
        """Requests data and converts it to JSON."""
        # Make request.
        parameters = {
            "lat": COORDINATES[0],
            "lon": COORDINATES[1],
            "appid": API_KEY,
            "exclude": "minutely,daily,alerts",
            "units": "metric"
        }

        response = requests.get(url=OWM_ENDPOINT, params=parameters)
        response.raise_for_status()

        # Convert raw data to JSON.
        self.weather_data = response.json()["current"]
        self.data = response.json()

    def get_current_weather(self):
        """Returns OWMs current weather."""
        # weather = {
        #     "temperature": round(float(self.weather_data["temp"]), 1),
        #     "feels_like": round(float(self.weather_data["feels_like"]), 1),
        #     "humidity": int(self.weather_data["humidity"]),
        #     "dew_point": round(float(self.weather_data["dew_point"]), 1),
        #     "wind_speed": round(float(self.weather_data["wind_speed"]), 1),
        #     "wind_direction": int(self.weather_data["wind_deg"])
        # }
        weather = [
            round(float(self.weather_data["temp"]), 1),
            round(float(self.weather_data["feels_like"]), 1),
            int(self.weather_data["humidity"]),
            round(float(self.weather_data["dew_point"]), 1),
            round(float(self.weather_data["wind_speed"]), 1),
            int(self.weather_data["wind_deg"])
            ]
        return weather
