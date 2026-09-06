lentoasemat = {}

lentoasemat["EFHK"] = "Helsinki-Vantaa"

while True:
    print("\nValitse")
    print("1. Syötä uusi lentoasema")
    print("2. Hae lentoaseman tiedot")
    print("3. Lopeta")

    valinta = input("Valitse 1, 2 tai 3: ")

    if valinta == "1":
        lentoasema_nimi = input("Lentoaseman nimi: ")
        lentoasema_koodi = input("Lentoaseman koodi: ")
        lentoasemat[lentoasema_koodi] = lentoasema_nimi

    if valinta == "2":
        lentoasema_koodi = input("ICAO koodi: ")
        if lentoasema_koodi in lentoasemat:
            print(lentoasemat[lentoasema_koodi])
        else:
            print("Lentoasemaa ei löydy")

    elif valinta == "3":
        break


