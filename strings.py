vorudi = input()
lvorudi = vorudi.lower()
def sedakhafekon(reshtam):
    biseda = ''
    for harf in range(0, len(reshtam)):
        if reshtam[harf] != 'a' and reshtam[harf] != 'o' and reshtam[harf] != 'u' and reshtam[harf] != 'i' and reshtam[harf] != 'e':
            biseda = biseda + reshtam[harf]
    return biseda
def noghtezan(reshtam):
    noghtedar =''
    for i in range(0,len(reshtam)):
        noghtedar = noghtedar + '.' + reshtam[i]
    return noghtedar
print(noghtezan(sedakhafekon(lvorudi)))