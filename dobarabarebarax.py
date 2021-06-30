vorudi = int (input())
yekan = vorudi % 10
dahgan = (vorudi % 100) // 10
sadghan = vorudi // 100

print (2 * ((yekan * 100) + (dahgan * 10) + sadghan))