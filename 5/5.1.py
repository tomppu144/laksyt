import random

maara = int(input("Kuinka monta noppaa: "))
summa = 0

for i in range(maara):
    silmaluku = random.randint(1, 6)
    summa = summa + silmaluku

print("Silmälukujen summa:", summa)