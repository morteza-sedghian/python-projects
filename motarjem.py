from collections import OrderedDict
tedadekalamat = int(input())
loghatname = dict()
tarjome = OrderedDict()

for i in range(0,tedadekalamat):
    khateJari = input()
    tempList = khateJari.split()
    loghatname[tempList[0]] = tempList[1]

jomle = input()
listeJomle = jomle.split()

for i in listeJomle:
    tarjome[i] = loghatname.get(i, i)
listeTarjome = tarjome.values()
print(' '.join(listeTarjome))
