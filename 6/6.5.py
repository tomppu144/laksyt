def parittomat(numerot):
    parilliset = []
    for luku in  numerot:
        if luku % 2 == 0:
            parilliset.append(luku)
    return parilliset


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
karsittu_lista = parittomat(lista)

print(f"Alkuperäinen lista: {lista}")
print(f"Karsittu lista: {karsittu_lista}")