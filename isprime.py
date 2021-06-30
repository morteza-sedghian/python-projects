vorudi = int (input())
count = 0
alayh = 1

while vorudi >= alayh:
    if vorudi % alayh == 0:
        count += 1
    alayh += 1

if count == 2:
    print('prime')
else:
    print('not prime')
