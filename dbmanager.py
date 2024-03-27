import mysql.connector

mydb = mysql.connector.connect(
    host="10.44.117.230",
    user="208259",
    password="952802",
    port="3386"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")  # baza.tabela albo podać db w connect

for x in mycursor:
    print(x)
