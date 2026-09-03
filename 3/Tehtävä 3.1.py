kuhan_pituus = float(input("kuhan pituus senttimetreinä: "))

sallittu_maara = 37

alin_maara = sallittu_maara - kuhan_pituus

if kuhan_pituus < 37:
    print(f"Laske kuha takaisin järveen, alimmasta sallitusta määrästä on {alin_maara} senttimetriä")
elif kuhan_pituus >= 37:
    print("Kuha on sallitun määrän pituinen")