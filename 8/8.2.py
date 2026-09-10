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

maakoodi = input("Anna maakoodi: ")

kursori = yhteys.cursor()

sql = "select type, COUNT(*) from airport where iso_country = %s group by type"
kursori.execute(sql, (maakoodi,))

tulokset = kursori.fetchall()

if tulokset:
    print(f"\nMaakoodin {maakoodi} lentokentät tyypeittäin:")
    for tyyppi, maara in tulokset:
        print(f"{tyyppi}: {maara} kpl")
else:
    print(f"Maakoodilla '{maakoodi}' ei löytynyt lentokenttiä.")

kursori.close()
yhteys.close()
