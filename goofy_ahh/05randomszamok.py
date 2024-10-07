"""Készíts egy rövid programot, amely 1 és 3 között generál véletlenszámot, majd összehasonlítja ezt a
 felhasználó által megadott, szintén ebbe a tartományba eső számmal! Az összehasonlítás eredményéről tájékoztassa
  a felhasználót!"""

import random

random_szam = random.randint(1, 3)
szam = int(input("Adj meg egy számot"))

if random_szam == szam:
    print("Eltaláltad!")
    print(f"A helyes szám {random_szam} volt.")
else:
    print(f"Nem találtad el. A helyes szám {random_szam} volt.")