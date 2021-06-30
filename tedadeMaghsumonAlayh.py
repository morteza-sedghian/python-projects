vorudi = 0
maxmaq = 0
num = 0
newtedad = 0
def tedad(adad):
    count = 0
    for maqsumalayh in range(1,adad+1):
        if adad % maqsumalayh == 0:
            count +=1
    return count

for i in range(20):
    vorudi = int(input())
    if tedad(vorudi) > maxmaq:
        maxmaq = tedad(vorudi)
        num = vorudi
    elif tedad(vorudi) == maxmaq and vorudi > num:
        num = vorudi
print(num, maxmaq)