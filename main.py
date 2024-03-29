from weather import MeteoWeather, OWMWeather


meteo = MeteoWeather()
owm = OWMWeather()

weather_raport = f"SGGW -> OWM: {owm.get_current_weather()}, Meteo: {meteo.get_current_temp()}\n"

# Check result
with open(file="data/raport.txt", mode="a", encoding="UTF-8") as raport:
    raport.write(weather_raport)

# Check data
print(owm.weather_data)
