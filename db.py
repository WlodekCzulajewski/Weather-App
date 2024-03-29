import mysql.connector
from mysql.connector.errors import DatabaseError


FOREIGN_HOST = "148.81.137.221"
EDUROM_HOST = "10.44.117.230"

try:
    mydb = mysql.connector.connect(
        host=EDUROM_HOST,
        user="208259",
        password="952802",
        port="3386"
    )
except DatabaseError:
    mydb = mysql.connector.connect(
        host=FOREIGN_HOST,
        user="208259",
        password="952802",
        port="3386"
    )

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")  # baza.tabela albo podać db w connect


for x in mycursor:
    print(x)
