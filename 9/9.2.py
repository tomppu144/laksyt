class Auto:

    def __init__(self, rekisteritunnus, huippunopeus,):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämän_hetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, nopeuden_muutos):
        uusi_nopeus = self.tämän_hetkinen_nopeus + nopeuden_muutos

        if uusi_nopeus > self.huippunopeus:
            self.tämän_hetkinen_nopeus = self.huippunopeus

        elif uusi_nopeus < 0:
            self.tämän_hetkinen_nopeus = uusi_nopeus

        else:
            self.tämän_hetkinen_nopeus = uusi_nopeus

if __name__ == "__main__":

    uusi_auto = Auto("ABC-123", 142)

    uusi_auto.kiihdytä(30)
    uusi_auto.kiihdytä(70)
    uusi_auto.kiihdytä(50)

    print(f"Nopeus kiihdytyksen jälkeen: {uusi_auto.tämän_hetkinen_nopeus} km/h")
    uusi_auto.kiihdytä(-200)
    print(f"Nopeus jarruttamisen jälkeen: {uusi_auto.tämän_hetkinen_nopeus} km/h")
