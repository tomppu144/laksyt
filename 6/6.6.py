import math

def yksikkohinta(halkaisija_cm, hinta_eur):
    sade_m = halkaisija_cm / 100 / 2
    pinta_ala = math.pi * sade_m ** 2
    return hinta_eur / pinta_ala

halkaisija1 = float(input("1. pizzan halkaisija (cm): "))
hinta1 = float(input("1. pizzan hinta (€): "))

halkaisija2 = float(input("2. pizzan halkaisija (cm): "))
hinta2 = float(input("2. pizzan hinta (€): "))

hinta_m2_1 = yksikkohinta(halkaisija1, hinta1)
hinta_m2_2 = yksikkohinta(halkaisija2, hinta2)

print(f"1. pizzan yksikköhinta: {hinta_m2_1:.2f} €/m²")
print(f"2. pizzan yksikköhinta: {hinta_m2_2:.2f} €/m²")

if hinta_m2_1 < hinta_m2_2:
    print("Ensimmäinen pizza on edullisempi!")
elif hinta_m2_2 < hinta_m2_1:
    print("Toinen pizza on edullisempi!")
else:
    print("Pizzoilla on sama yksikköhinta!")