"""Thonny fejlesztői környezetben készíts egy rövid programot,
amely a felhasználótól bekéri a kör sugarát, és ennek alapján kiszámolja a kör kerületét és területét!"""

PI = 3.14

adat = input("Add meg a kör sugarát!  ")
r = int(adat)

print("Kör kerülete:")
print (int(2*r*PI))
print("kör területe: ")
print(r*r*PI)