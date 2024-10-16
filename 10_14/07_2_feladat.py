"""Készíts egy programot, amely egymásba ágyazott
ciklusok segítségével rajzolja ki egy 5 x 5-ös mezőben
az alábbi alakzatot!

O . . . .
. O . . .
. . O . .
. . . O .
. . . . O"""

"""for i in range(5):
    for j in range(5):
        if j == i:
            print("0", end=" ")
        else:
            print(".", end=" ")
    print()"""


"""Készíts egy programot, amely egymásba ágyazott 
ciklusok segítségével rajzolja ki egy 7 x 7-es mezőben
az alábbi alakzatot!

O . . . . . O 
. O . . . O .
. . O . O . .
. . . O . . .
. . O . O . .
. O . . . O .
O . . . . . O """


szam = int(input("Adj meg egy számot!"))
for i in range(szam):
    for j in range(szam):
        if j == i:
            print("O", end=" ")
        elif j + i == 6:
            print("O", end=" ")
        else:
            print(".", end=" ")
    print()

    
