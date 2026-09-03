luvut = []

while True:
    luku = input("Anna lukuja: ")

    if luku == "":
        break

    else:
        luku_numerona = int(luku)
        luvut.append(luku_numerona)

luvut.sort(reverse=True)

print(luvut[:5])