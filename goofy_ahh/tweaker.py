"""Készíts egy programot, amely a felhasználótól két külön kérdésben megkérdezi, hogy az ikrek (Henrik és Hanna) jönnek-e ma kosrazni!
 Például így: Jön Henrik ma kosarazni? (igen/nem). A program írja ki, hogy melyik állítás igaz az alábbiak közül:
- egyikük sem jön kosarazni,
- mind a ketten jönnek kosarazni,
- csak az egyikük jön kosarazni."""

henrik = input("Jön Henrik kosarazni? ")

hanna = input("Jön Hanna kosarazni? ")

if henrik == "Igen" and hanna == "Igen" :
    print("Mindketten jönnek kosarazni!")

elif henrik == "Igen" and hanna == "Nem":
    print("Csak Henrik jön kosarazni.")

elif henrik == "Nem" and hanna == "Igen":
    print("Csak Hanna jön kosarazni.")

elif henrik == "Nem" and hanna == "Nem":
    print("Egyikük se jön kosarazni.")