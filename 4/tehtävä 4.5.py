salasana = "rules"
kayttajatunnus = "python"

yritykset = 0

while yritykset < 5:
    syote = input("Käyttäjätunnus: ")
    salasanasyote = input("Salasana: ")

    if syote == kayttajatunnus and salasanasyote == salasana:
        print("Tervetuloa")
        break
    else:
        yritykset += 1

    if yritykset == 5:
        print("Pääsy evätty")