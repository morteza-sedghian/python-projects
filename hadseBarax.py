import random
min = 1
max = 99
hads = random.randint(min, max)
Chetoram = input(hads)

while Chetoram != 'd':
    if Chetoram == 'b':
        min = hads + 1
    elif Chetoram == 'k':
        max = hads - 1
    else:
        print('Gheire Ghabele Ghabule')
        break
    hads = random.randint(min, max)
    Chetoram = input(hads)
