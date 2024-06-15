import tkinter
from db import DBMANAGER
import json


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Arial"


def get_current_weather():
    db = DBMANAGER()
    weather_data = db.get_last_record()
    weather_label.config(text=f"Time: {weather_data[0]},\n"
                              f"Temperature: {weather_data[1]},\n"
                              f"Feels like: {weather_data[3]},\n"
                              f"Humidity: {weather_data[5]},\n"
                              f"Dew point: {weather_data[7]},\n"
                              f"Wind speed: {weather_data[9]},\n"
                              f"Wind direction: {weather_data[11]}\n",
                              fg=PINK)

    tomorrow_data = json.loads(weather_data[13])[23]
    tomorrow_label.config(text=f"Time of forecast: 24h,\n"
                              f"Temperature: {tomorrow_data["temperature"]},\n"
                              f"Feels like: {tomorrow_data["feels_like"]},\n"
                              f"Humidity: {tomorrow_data["humidity"]},\n"
                              f"Dew point: {tomorrow_data["dew_point"]},\n"
                              f"Wind speed: {tomorrow_data["wind_speed"]},\n"
                              f"Wind direction: {tomorrow_data["wind_direction"]}\n",
                                fg=PINK)

    after_tomorrow_data = json.loads(weather_data[13])[47]
    after_tomorrow_label.config(text=f"Time of forecast: 48h,\n"
                              f"Temperature: {after_tomorrow_data["temperature"]},\n"
                              f"Feels like: {after_tomorrow_data["feels_like"]},\n"
                              f"Humidity: {after_tomorrow_data["humidity"]},\n"
                              f"Dew point: {after_tomorrow_data["dew_point"]},\n"
                              f"Wind speed: {after_tomorrow_data["wind_speed"]},\n"
                              f"Wind direction: {after_tomorrow_data["wind_direction"]}\n",
                                fg=PINK)

def get_last_48h():
    db = DBMANAGER()
    data = db.get_last_48h()
    statistic = {
        "Temperature": 0,
        "Feels like": 0,
        "Humidity": 0,
        "Dew point": 0,
        "Wind speed": 0,
        "Wind direction": 0
    }

    for record in data:
        statistic["Temperature"] += record[1] - record[2]
        statistic["Feels like"] += record[3] - record[4]
        statistic["Humidity"] += record[5] - record[6]
        statistic["Dew point"] += record[7] - record[8]
        statistic["Wind speed"] += record[9] - record[10]
        statistic["Wind direction"] += record[11] - record[12]
    for key in statistic:
        statistic[key] = abs(round(statistic[key] / 48, 1))

    print(statistic)

    statistic_label.config(text=f"Average Difference\n"
                                f"Temperature: {statistic["Temperature"]},\n"
                                f"Feels like: {statistic["Feels like"]},\n"
                                f"Humidity: {round(statistic["Humidity"])},\n"
                                f"Dew point: {statistic["Dew point"]},\n"
                                f"Wind speed: {statistic["Wind speed"]},\n"
                                f"Wind direction: {round(statistic["Wind direction"])}\n",
                              fg=PINK)

window = tkinter.Tk()
window.title("Weather")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = tkinter.Label(text="Weather App", fg=PINK, bg=YELLOW, font=(FONT_NAME, 50), pady=20)
title_label.grid(column=1, row=0)

weather_label = tkinter.Label(text="", fg=PINK, bg=YELLOW, font=(FONT_NAME, 18), pady=20)
weather_label.grid(column=0, row=1)

tomorrow_label = tkinter.Label(text="", fg=PINK, bg=YELLOW, font=(FONT_NAME, 18), pady=20)
tomorrow_label.grid(column=1, row=1)

after_tomorrow_label = tkinter.Label(text="", fg=PINK, bg=YELLOW, font=(FONT_NAME, 18), pady=20)
after_tomorrow_label.grid(column=2, row=1)

get_weather_button = tkinter.Button(text="Get Weather", highlightbackground=YELLOW, command=get_current_weather)
get_weather_button.grid(column=1, row=2)

statistic_label = tkinter.Label(text="", fg=PINK, bg=YELLOW, font=(FONT_NAME, 18), pady=20)
statistic_label.grid(column=1, row=3)

get_statistic_button = tkinter.Button(text="Get Statistic", highlightbackground=YELLOW, command=get_last_48h)
get_statistic_button.grid(column=1, row=4)

window.mainloop()
