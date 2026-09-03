import random

koodi1 = ""
for _ in range(3):
    koodi1 += str(random.randint(0, 9))

koodi2 = ""
for _ in range(4):
    koodi2 += str(random.randint(1, 6))

print(f"Kolmenumeroinen koodi (0-9): {koodi1}")
print(f"Nelinumeroinen koodi (1-6): {koodi2}")