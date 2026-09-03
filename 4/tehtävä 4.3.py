luvut = []

while True:
    syote = input("Anna lukuja: ")

    if syote == "":
        break
    else:
        luku = int(syote)
        luvut.append(luku)


if luvut == []:
    print(syote)
else:
    pienin = min(luvut)
    suurin = max(luvut)
    print("Pienin luku:", pienin)
    print("Suurin luku:", suurin)