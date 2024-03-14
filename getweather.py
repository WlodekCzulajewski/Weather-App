from bs4 import BeautifulSoup
import requests

class RealWeather:
    """Class responsible for getting real current weather."""

    def __init__(self):
        """Requests webpage source 'html' and creates Beautiful Soup."""
        self.meteo_endpoint = "https://sggw.meteo.waw.pl/"

        # Request webpage source
        response = requests.get(url=self.meteo_endpoint)
        response.raise_for_status()
        meteo_web_page = response.text

        # Create soup object
        self.soup = BeautifulSoup(meteo_web_page, "html.parser")

    def get_current_temp(self):
        """Returns current temperature."""
        return self.soup.find(name="div", class_="plotbox_title").getText().split()[1]
