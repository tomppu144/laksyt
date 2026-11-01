class Hissi:
    def __init__(self, alin_kerros: int, ylin_kerros: int):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def kerros_ylos(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}.")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}.")

    def siirry_kerrokseen(self, kohdekerros: int):
        if kohdekerros < self.alin_kerros or kohdekerros > self.ylin_kerros:
            print(
                f"Virhe: Kerros {kohdekerros} on sallittujen rajojen ({self.alin_kerros}-{self.ylin_kerros}) ulkopuolella.")
            return

        print(f"Siirrytään kerroksesta {self.nykyinen_kerros} kohteeseen {kohdekerros}...")

        while self.nykyinen_kerros < kohdekerros:
            self.kerros_ylos()
        while self.nykyinen_kerros > kohdekerros:
            self.kerros_alas()


class Talo:
    def __init__(self, alin_kerros: int, ylin_kerros: int, hissien_lukumaara: int):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = [Hissi(alin_kerros, ylin_kerros) for _ in range(hissien_lukumaara)]

    def aja_hissia(self, hissin_numero: int, kohdekerros: int):
        if 1 <= hissin_numero <= len(self.hissit):
            print(f"\nAjetaan hissiä numero {hissin_numero}:")
            valittu_hissi = self.hissit[hissin_numero - 1]
            valittu_hissi.siirry_kerrokseen(kohdekerros)
        else:
            print(f"Virhe: Hissiä numero {hissin_numero} ei ole olemassa (talossa on hissit 1-{len(self.hissit)}).")


if __name__ == "__main__":
    talo = Talo(1, 10, 3)

    print(f"Talo luotu. Kerrokset: {talo.alin_kerros}-{talo.ylin_kerros}, Hissien määrä: {len(talo.hissit)}")

    talo.aja_hissia(1, 5)
    talo.aja_hissia(2, 8)
    talo.aja_hissia(1, 1)