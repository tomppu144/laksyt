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


if __name__ == "__main__":
    hissi = Hissi(1, 7)

    print(f"Hissi luotu. Alin kerros: {hissi.alin_kerros}, Ylin kerros: {hissi.ylin_kerros}")
    print(f"Hissi on alussa kerroksessa {hissi.nykyinen_kerros}.\n")

    hissi.siirry_kerrokseen(5)

    print("-" * 30)

    hissi.siirry_kerrokseen(hissi.alin_kerros)