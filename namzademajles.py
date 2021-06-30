vorudi = int(input())
max = 0
while vorudi != -1:
    if vorudi > max:
        max = vorudi
    vorudi = int(input())
print(max)