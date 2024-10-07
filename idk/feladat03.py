"""Írj egy programot, ami a felhasználótól bekéri először a keresztnevét,
majd a vezetéknevét. A program ezután összefűzi ezeket egy teljes_nev nevű változóba. Végül a program a teljes nevén üdvözli a felhasználót!"""

vezetek_nev = input("Adja meg a vezeték nevét!")
kereszt_nev = input("Adja meg a kereszt nevét!")

teljes_nev = vezetek_nev + " " + kereszt_nev

print(f"Üdv, {teljes_nev}!")