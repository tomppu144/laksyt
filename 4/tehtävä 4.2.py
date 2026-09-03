while True:
    tuumat = float(input('tuumat: '))

    if tuumat < 0:
        break

    sentit = tuumat * 2.54
    print(f"{sentit}cm")