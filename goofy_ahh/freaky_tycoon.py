"""Készíts egy programot, amely a felhasználótól bekér egy egész számot, majd megvizsgálja, hogy a megadott szám
- pozitív páros vagy
- negatív páratlan.
Az eredményről tájékoztatja a felhasználót."""

szam = int(input("Mondj egy számot!"))
if szam % 2 == 0 and szam > 0:
    print("Ez egy páros pozitív szám")

elif szam % 2 != 0 and szam < 0:
    print("Ez egy páratlan negatív szám! ")

else:
    print("Nem felel meg ez a szám!")
