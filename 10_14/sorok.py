"""sor = 1
while sor <= 4:
    oszlop = 1
    while oszlop <= 7:
        print('O ' , end='')
        oszlop = oszlop + 1
    print('')
    sor = sor + 1"""

"""szam = int(input("Adj meg egy páros számot!"))
if szam % 2 == 0:
    szam = True

darab_karakter = 1
sor = 1
while sor <= 7:
    oszlop = 1
    while oszlop <= darab_karakter:
        print('O ', end='')
        oszlop = oszlop + 1
    print('')
    darab_karakter = darab_karakter + 1
    sor = sor + 1"""


szam = int(input("Adj meg egy páros számot!"))
if szam % 2 == 0:
    darab_karakter = 1
    sor = 1
    while sor <= szam:
        oszlop = 1
        while oszlop <= darab_karakter:
            print('O ', end='')
            oszlop = oszlop + 1
        print('')
        darab_karakter = darab_karakter + 1
        sor = sor + 1
