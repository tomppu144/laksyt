import random


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämän_hetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, nopeuden_muutos):
        uusi_nopeus = self.tämän_hetkinen_nopeus + nopeuden_muutos

        if uusi_nopeus > self.huippunopeus:
            self.tämän_hetkinen_nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.tämän_hetkinen_nopeus = 0
        else:
            self.tämän_hetkinen_nopeus = uusi_nopeus

    def kulje(self, tuntimäärä):
        self.kuljettu_matka += self.tämän_hetkinen_nopeus * tuntimäärä


class Kilpailu:
    def __init__(self, nimi: str, pituus_km: int, autot: list):
        self.nimi = nimi
        self.pituus_km = pituus_km
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            muutos = random.randint(-10, 15)
            auto.kiihdytä(muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"\n{'Rekisteritunnus':<15} | {'Huippunopeus':<15} | {'Nopeus nyt':<15} | {'Kuljettu matka'}")
        print(f"{'-'*15}-+-{'-'*15}-+-{'-'*15}-+-{'-'*15}")
        for auto in self.autot:
            print(f"{auto.rekisteritunnus:<15} | {auto.huippunopeus:<15} | {auto.tämän_hetkinen_nopeus:<15} | {auto.kuljettu_matka:.1f} km")

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus_km:
                return True
        return False


# Pääohjelma
if __name__ == "__main__":
    autolista = []
    for i in range(1, 11):
        rekisteritunnus = f"ABC-{i}"
        huippunopeus = random.randint(100, 200)
        autolista.append(Auto(rekisteritunnus, huippunopeus))

    romuralli = Kilpailu("Suuri romuralli", 8000, autolista)

    print(f"Kilpailu '{romuralli.nimi}' ({romuralli.pituus_km} km) on alkanut!\n")

    tunteja_kulunut = 0

    while not romuralli.kilpailu_ohi():
        romuralli.tunti_kuluu()
        tunteja_kulunut += 1

        if tunteja_kulunut % 10 == 0:
            print(f"Tilanne {tunteja_kulunut} tunnin jälkeen")
            romuralli.tulosta_tilanne()
            print()

    print(f"\n{'='*65}")
    print(f" Kilpailu päättyi! Voittaja on ratkennut {tunteja_kulunut} tunnin jälkeen.")
    print(f"{'='*65}")
    romuralli.tulosta_tilanne()
    print(f"{'='*65}")