from weather import METEO, OWM
from db import DBMANAGER

if __name__ == "__main__":
    meteo = METEO()
    weather = meteo.get_current_weather()
    owm = OWM()
    owm_cw = owm.get_current_weather()
    forecast = owm.get_forecast()
    for i in owm_cw:
        weather.append(i)
    weather.append(forecast)

    db = DBMANAGER()
    db.save_measurements(val=tuple(weather))
    # column = input("Write column name: ")
    # db.get_records(column)
