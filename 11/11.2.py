class Auto:
    def __init__(self, rekisteritunnus: str, huippunopeus: int):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämän_hetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, nopeuden_muutos: int):
        uusi_nopeus = self.tämän_hetkinen_nopeus + nopeuden_muutos

        if uusi_nopeus > self.huippunopeus:
            self.tämän_hetkinen_nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.tämän_hetkinen_nopeus = 0
        else:
            self.tämän_hetkinen_nopeus = uusi_nopeus

    def kulje(self, tuntimäärä: float):
        self.kuljettu_matka += self.tämän_hetkinen_nopeus * tuntimäärä


class Sähköauto(Auto):
    def __init__(self, rekisteritunnus: str, huippunopeus: int, akkukapasiteetti_kwh: float):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti_kwh = akkukapasiteetti_kwh


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus: str, huippunopeus: int, bensatankki_litraa: float):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankki_litraa = bensatankki_litraa


# Pääohjelma
if __name__ == "__main__":
    sahkoauto = Sähköauto("ABC-15", 180, 52.5)
    polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

    sahkoauto.kiihdytä(120)
    polttomoottoriauto.kiihdytä(100)

    tuntimaara = 3
    sahkoauto.kulje(tuntimaara)
    polttomoottoriauto.kulje(tuntimaara)

    print("Autojen tiedot ajon jälkeen (3 tuntia)")
    print(f"Sähköauto ({sahkoauto.rekisteritunnus}):")
    print(f"Huippunopeus: {sahkoauto.huippunopeus} km/h")
    print(f"Akkukapasiteetti: {sahkoauto.akkukapasiteetti_kwh} kWh")
    print(f"Matkamittarilukema: {sahkoauto.kuljettu_matka} km")

    print()

    print(f"Polttomoottoriauto ({polttomoottoriauto.rekisteritunnus}):")
    print(f"Huippunopeus: {polttomoottoriauto.huippunopeus} km/h")
    print(f"Bensatankki: {polttomoottoriauto.bensatankki_litraa} l")
    print(f"Matkamittarilukema: {polttomoottoriauto.kuljettu_matka} km")