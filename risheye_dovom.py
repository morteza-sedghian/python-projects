import decimal
from math import sqrt
from math import floor
tedad = int(input())
listeVorudi = []

for i in range(0,tedad):
    listeVorudi.append(int(input()))
for i in listeVorudi:
    ghableFormat = floor(sqrt(i) * 10000)
    ghableFormat = ghableFormat / 10000
    print(format(ghableFormat, '.4f'))
