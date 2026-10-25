class Auto:

    def __init__(self, rekisteritunnus, huippunopeus,):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämän_hetkinen_nopeus = 0
        self.kuljettu_matka = 0



if __name__ == "__main__":

    uusi_auto = Auto("ABC-123", 142)

    print(f"Rekisteritunnus: {uusi_auto.rekisteritunnus}")
    print(f"Huippunopeus: {uusi_auto.huippunopeus}")
    print(f"tämän_hetkinen_nopeus: {uusi_auto.kuljettu_matka} km/h")
    print(f"Kuljettu matka: {uusi_auto.kuljettu_matka} km")