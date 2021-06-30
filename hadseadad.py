import random
number = random.randint(1,100)
hads = int(input('adad ro hads bezan: '))
while hads != number:
    if hads < number:
        print('boro bala')
    else:
        print('bia paiin')
    hads = int(input('dobare adad ro hads bezan: '))
print('Rahmat Bar Un Shiri Ke To Ro Khord!!!')    