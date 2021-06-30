vorudi = input()
tedademoghayese = len(vorudi) // 2
vorudi = vorudi.lower()

for i in range(0, tedademoghayese):
    if vorudi[i] != vorudi[len(vorudi) - 1 - i]:
        print('not palindrome')
        exit()
print('palindrome')