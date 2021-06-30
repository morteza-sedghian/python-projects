vorudi = int(input())
max = 0
second = 0
while vorudi != -1:
    if vorudi > max:
        second = max
        max = vorudi
    elif vorudi > second:
        second = vorudi
    vorudi = int(input())
print(max, second)