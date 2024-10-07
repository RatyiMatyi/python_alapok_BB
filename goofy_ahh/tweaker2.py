"""Készíts egy programot, amely a felhasználó által megadott egész számról eldönti, hogy
- csak 3-mal osztható,
- csak 4-gyel osztható,
- 3-mal és 4-gyel is osztható,
- sem 3-mal, sem 4-gyel nem osztható!"""

szam = int(input("Adj megy egy számot!"))

if szam % 3 == 0 and szam %4 == 0 :
    print("Ez a szám 3-mal és 4-gyel is osztható")

elif szam % 3 == 0 :
    print("Ez a szám 3-al osztható.")

elif szam % 4 == 0 :
    print("Ez a szám 4-el osztható.")

elif szam % 4 != 0 and szam % 3 != 0:
    print("Sem 3-mal, sem 4-gyel nem osztható")