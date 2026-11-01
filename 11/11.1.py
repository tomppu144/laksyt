class Julkaisu:
    def __init__(self, nimi: str):
        self.nimi = nimi


class Kirja(Julkaisu):
    def __init__(self, nimi: str, kirjoittaja: str, sivumaara: int):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        print(f"Kirja: {self.nimi}")
        print(f"Kirjailija: {self.kirjoittaja}")
        print(f"Sivumäärä: {self.sivumaara} sivua")


class Lehti(Julkaisu):
    def __init__(self, nimi: str, paatoimittaja: str):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print(f"Lehti: {self.nimi}")
        print(f"Päätoimittaja: {self.paatoimittaja}")


# Pääohjelma
if __name__ == "__main__":
    aku_ankka = Lehti("Aku Ankka", "Aki Hyyppä")
    hytti_no_6 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

    print("Julkaisujen tiedot")
    aku_ankka.tulosta_tiedot()
    print()
    hytti_no_6.tulosta_tiedot()