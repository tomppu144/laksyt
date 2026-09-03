sukupuoli = input("Kerro sukupuolesi: ")
hemoglobiiniarvo = int(input("Kerro hemoglobiarvo (g/l): "))

if sukupuoli == "nainen":
    if hemoglobiiniarvo < 117:
        print("Hemoglobiiniarvo on alhainen")
    elif hemoglobiiniarvo <= 175:
        print("Hemoglobiiniarvo on normaali")
    if hemoglobiiniarvo > 175:
        print("Hemoglobiiniarvo on korkea")



elif sukupuoli == "mies":
    if hemoglobiiniarvo < 134:
        print("Hemoglobiiniarvo on alhainen")
    elif hemoglobiiniarvo <= 195:
        print("Hemoglobiiniarvo on normaali")
    if hemoglobiiniarvo > 195:
        print("Hemoglobiiniarvo on korkea")