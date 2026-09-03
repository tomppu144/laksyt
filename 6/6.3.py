def galloonat_litroiksi(galloonat):

    maara = galloonat * 3.785
    return maara

galloonamaara = float(input("Anna Galloonien määrä: "))

while galloonamaara >= 0:
    litrat = galloonat_litroiksi(galloonamaara)
    print(f"{galloonamaara} galloonaa on {litrat} litraa.")

    galloonamaara = float(input("Anna Galloonien määrä: "))