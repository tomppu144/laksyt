import random

def heita_noppaa(tahkot):
    return random.randint(1,tahkot)


maksimi = int(input("Kuinka monta tahkoa: "))

tulos = 0

while tulos != maksimi:
    tulos = heita_noppaa(maksimi)
    print(tulos)
