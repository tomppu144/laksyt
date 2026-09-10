import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='uskomatontabreinii',
         autocommit=True,
         collation="utf8mb4_unicode_ci"
         )

icao = input("Syötä ICAO koodi: ")

kursori = yhteys.cursor()

sql = "select name, municipality from airport where ident = %s"
kursori.execute(sql, (icao,))

tulos = kursori.fetchone()

if tulos:
    nimi, kunta = tulos
    print(f"Lentoaseman nimi: {nimi}")
    print(f"Lentoaseman kunta: {kunta}")
else:
    print(f"Lentoasemaa ICAO koodilla ei löytynyt.")

kursori.close()
yhteys.close()