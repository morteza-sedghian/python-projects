jam = 0
bord = 0
for game in range(30):
    emtiaz = int(input())
    if emtiaz == 3:
        bord += 1
    jam += emtiaz
print(jam,bord)