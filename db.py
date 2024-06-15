import mysql.connector
from mysql.connector.errors import DatabaseError
from mysql.connector.plugins import mysql_native_password
import datetime

FOREIGN_HOST = "148.81.137.221"
EDUROM_HOST = "10.44.117.230"


class DBMANAGER:
    """Class responsible for managing database."""

    def __init__(self):
        """Crete cursor on initialization."""

        # Automatically connects to right database
        try:
            self.mydb = mysql.connector.connect(
                host=EDUROM_HOST,
                user="208259",
                password="952802",
                port="3386",
                database="208259_ppi"
            )
        except DatabaseError:
            self.mydb = mysql.connector.connect(
                host=FOREIGN_HOST,
                user="208259",
                password="952802",
                port="3386",
                database="208259_ppi"
            )

        self.mycursor = self.mydb.cursor()

    def save_measurements(self, val):
        """Saves taken measurements."""
        sql = "INSERT INTO weather (meteo_temperature, meteo_feels_like, meteo_humidity, meteo_dew_point, meteo_wind_speed, meteo_wind_direction, owm_temperature, owm_feels_like, owm_humidity, owm_dew_point, owm_wind_speed, owm_wind_direction, forecast) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        print(self.mycursor.rowcount, "record inserted.")

    def get_last_record(self):
        """Fetches last record from database"""
        self.mycursor.execute(f"SELECT * FROM weather order by time desc limit 1")
        result = self.mycursor.fetchall()[0]

        return result

    def get_last_48h(self):
        """Fetches last 48h records from database"""
        self.mycursor.execute(f"SELECT * FROM weather order by time desc limit 48")
        result = self.mycursor.fetchall()

        return result
