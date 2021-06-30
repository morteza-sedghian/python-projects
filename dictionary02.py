reshte = 'Salam. Man injamo daram ye barname test mikonam'
shomarande = dict()

for letter in reshte:
    shomarande[letter] = shomarande.get(letter, 0) + 1
for this_one in list(shomarande.keys()):
    print('%s appeared %s times' % (this_one, shomarande[this_one]))