from weather import MeteoWeather, OWMWeather


meteo = MeteoWeather()
meteo_cw = meteo.get_current_weather()
owm = OWMWeather()
owm_cw = owm.get_current_weather()

# Create raport
with open(file="data/raport.txt", mode="a", encoding="UTF-8") as raport:
    # raport.write("Meteo - OWM\n")
    for key, value in meteo_cw.items():
        raport.write(f"{key.title():20s} {value} - {owm_cw[key]}\n")

# Check data
print(owm.weather_data)
