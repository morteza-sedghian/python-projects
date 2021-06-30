vorudi = input()
list_vorudi = vorudi.split()
list_vorudi[0] = int(list_vorudi[0])
list_vorudi[1] = int(list_vorudi[1])
list_vorudi[2] = int(list_vorudi[2])
list_vorudi.sort()

print((list_vorudi[1] - list_vorudi[0]) + (list_vorudi[2] - list_vorudi[1]))

