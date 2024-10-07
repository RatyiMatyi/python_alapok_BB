"""Készíts egy programot, amely megkérdezi a felhasználótól, hogy jó napja van-e! A válasz kétféle lehet: igen
vagy nem. A választól függően írjon ki üzenetet a gép!"""

valasz = input("Jó a napod? ")
valasz_lowercase = valasz.lower()
if valasz_lowercase == "igen":
        print("Remélem így is marad ")
elif valasz_lowercase == "nem" :
        print("Remélem jobb lesz ")
elif valasz_lowercase == "diddy" :
        print("szeretnél a tusolóban cigizni? ")
else:
        print("Sajnos nem értem a válaszodat! ")

