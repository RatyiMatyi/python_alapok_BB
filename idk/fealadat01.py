"""Thonny fejlesztői környezetben készíts egy rövid programot, amely
kommentként tartalmazza a program funkciójának leírását,
konstansként tárolja PI értékét,
egy másik változóban tárolja egy kör sugarának nagyságát (cm-ben megadva),
kiszámolja és a képernyőre kiírja a kör kerületét és területét!"""

PI = 3.14
r = 5
kerulet = r*r*PI    #kör kerületének képlete
terulet = int(2 * r * PI)    #kör területének képlete

print( f"A kör területe: {terulet}" + "cm")
print(f"A kör kerülete: {kerulet}" + "cm")

"""Készíts egy rövid programot, amely egy változóban eltárol egy szót. Próbáld meg ennek a változónak a tartalmát int értékké átalakítani.
Mit tapasztalsz? Milyen üzenet jelenik meg a képernyőn?"""

valatozo_1 = int(float('gtr'))

print(valatozo_1)
#ValueError: could not convert string to float: 'gtr'


"""Készíts egy rövid programot, amelyben egy olyan változó értékét szeretnéd kiíratni, ami előzőleg nem is szerepel a
 kódodban. Hogyan jelöli a fejlesztői környezet a hibát? Futtasd! Milyen hibaüzenetet kapsz?"""
szotyi = "jó"

print(szotyi)
print()