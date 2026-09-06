nimet = set()

while True:
    nimi = input("Kerro nimi: ")
    if nimi == "":
        break
    if nimi in nimet:
        print("Nimi on jo syötetty")
    else:
        print("Uusi nimi")
        nimet.add(nimi)

for nimi in nimet:
    print(nimi)