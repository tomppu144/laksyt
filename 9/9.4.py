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


if __name__ == "__main__":
    autot = []
    for i in range(1, 11):
        rekisteritunnus = f"ABC-{i}"
        huippunopeus = random.randint(100, 200)
        autot.append(Auto(rekisteritunnus, huippunopeus))

    # 2. Kilpailun simulaatio
    kilpailu_kaynnissa = True
    tuntimäärä = 0

    while kilpailu_kaynnissa:
        tuntimäärä += 1
        for auto in autot:
            muutos = random.randint(-10, 15)
            auto.kiihdytä(muutos)

            auto.kulje(1)

            if auto.kuljettu_matka >= 10000:
                kilpailu_kaynnissa = False

    print(f"\n{'=' * 65}")
    print(f" KILPAILU PÄÄTTYI! Kilpailu kesti {tuntimäärä} tuntia.")
    print(f"{'=' * 65}")
    print(f"{'Rekisteritunnus':<15} | {'Huippunopeus':<15} | {'Nopeus nyt':<15} | {'Kuljettu matka'}")
    print(f"{'-' * 15}-+-{'-' * 15}-+-{'-' * 15}-+-{'-' * 15}")

    for auto in autot:
        print(
            f"{auto.rekisteritunnus:<15} | {auto.huippunopeus:<15} | {auto.tämän_hetkinen_nopeus:<15} | {auto.kuljettu_matka:.1f} km")
    print(f"{'=' * 65}")