from weather import Meteo, OWM
from db import DB_Manager

meteo = Meteo()
weather = meteo.get_current_weather()
owm = OWM()
owm_cw = owm.get_current_weather()
db = DB_Manager()

for i in owm_cw:
    weather.append(i)

db.save_measurements(val=tuple(weather))
