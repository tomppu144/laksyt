def summa(luvut):
    koko_summa = 0
    for luku in luvut:
        koko_summa += luku
    return koko_summa



lista = [1, 2, 3, 4, 5, 6]

tulos = summa(lista)
print(tulos)