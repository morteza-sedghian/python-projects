tedad = int(input())
vorudi = input()
vorudi = vorudi.split()

for i in range(0, len(vorudi)):
    vorudi[i] = int(vorudi[i])

darDastras = 0
for i in range(0,len(vorudi)):
    if vorudi[i] < 3:
        darDastras = darDastras + 1

print(darDastras // 3)
