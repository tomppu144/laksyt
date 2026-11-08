
import requests

api_avain = "85e532df0bc3e3346e4277e848804483"

paikkakunta = input("Anna paikkakunta: ")


geo_url = "https://api.openweathermap.org/geo/1.0/direct"

geo_vastaus = requests.get(geo_url, params={
    "q": paikkakunta,
    "limit": 1,
    "appid": api_avain
})

paikat = geo_vastaus.json()

if not paikat:
    print("Paikkakuntaa ei löytynyt.")
else:
    lat = paikat[0]["lat"]
    lon = paikat[0]["lon"]

    saa_url = "https://api.openweathermap.org/data/2.5/weather"

    vastaus = requests.get(saa_url, params={
        "lat": lat,
        "lon": lon,
        "appid": api_avain,
        "lang": "fi"
    })

    tiedot = vastaus.json()

    saatila = tiedot["weather"][0]["description"]
    lampotila_kelvin = tiedot["main"]["temp"]

    # Muunnetaan Kelvin Celsius-asteiksi
    lampotila_celsius = lampotila_kelvin - 273.15

    print(f"Säätila: {saatila}")
    print(f"Lämpötila: {lampotila_celsius:.1f} °C")
