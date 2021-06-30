vorudi = input()
lower = 0
upper = 0
for harf in(vorudi):
    if harf.islower():
        lower = lower + 1
    elif harf.isupper():
        upper = upper + 1

if upper > lower:
    print(vorudi.upper())
else:
    print(vorudi.lower())
