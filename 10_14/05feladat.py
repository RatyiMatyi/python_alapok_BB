"""Írj egy programot, amely a felhasználótól páros számot kér be. Amennyiben a
megadott szám páratlan, újra és újra megtörténik az adatbekérés mindaddig, amíg végül páros számot nem ad meg a felhasználó."""

paros_szam = False

while paros_szam == False:
    valasz = int(input("Adj meg egy páros számot"))
    if valasz % 2 == 0:
        print("Köszönöm")
        paros_szam = True

