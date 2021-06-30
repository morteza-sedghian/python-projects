vorudi = input()
if 'AB' not in vorudi or 'BA' not in vorudi:
    print('NO')
    exit()
else:
    vorudibeAB = vorudi[:(vorudi.find('AB'))]+ ' ' + vorudi[(vorudi.find('AB') + 2):]
    vorudibeBA = vorudi[:(vorudi.find('BA'))]+ ' ' + vorudi[(vorudi.find('BA') + 2):]

if 'BA' not in vorudibeAB and 'AB' not in vorudibeBA:
    print('NO')
    exit()
else:
    print('YES')
