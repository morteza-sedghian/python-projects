from collections import OrderedDict
tedadeAra = int(input())
ara = []
natije = OrderedDict()

for i in range(0, tedadeAra):
    ara.append(input())
ara.sort()
for ray in ara:
    natije[ray] = natije.get(ray, 0) + 1
for i in list(natije.keys()):
    print(i, natije[i])
