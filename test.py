import csv
with open('D:\learning\python\input.csv') as f:
    reader = csv.reader(f)
    for i in reader:
        print(type(i))