tedad = int(input())
laptop_info = []

for i in range(0,tedad):
    temp_vorudi = input()
    temp_vorudi = temp_vorudi.split()
    temp_vorudi[0] = int(temp_vorudi[0])
    temp_vorudi[1] = int(temp_vorudi[1])
    laptop_info.append(temp_vorudi)

laptop_info.sort()

for i in range(0, (tedad - 1)):
    arzun = laptop_info[i]
    gerun = laptop_info[i+1]
    if arzun[0] != gerun[0]:
        for j in range((i+1), tedad):
            temp = laptop_info[j]
            if arzun[1] > temp[1]:
                print('happy irsa')
                exit()
print('poor irsa')

