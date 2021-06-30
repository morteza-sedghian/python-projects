vorudi = input()
yekha = vorudi.count('1')
doha = vorudi.count('2')
seha = vorudi.count('3')

def morattabsaz(yek, do, se):
    morattab = ''
    for i in range (0,yekha):
        morattab = morattab + '1' + '+'
    for i in range (0,doha):
        morattab = morattab + '2' + '+'
    for i in range (0,seha):
        morattab = morattab + '3' + '+'
    morattab = morattab[:(len(morattab) - 1)]

    return morattab

print(morattabsaz(yekha, doha, seha))