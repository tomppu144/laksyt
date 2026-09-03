import random

oikea_luku = random.randint(1,10)

while True:
    arvaus = int(input("Arvaa luku: "))

    if arvaus > oikea_luku:
        print("Liian suuri")
    elif arvaus < oikea_luku:
        print("Liian pieni")
    else:
        print("Oikein")