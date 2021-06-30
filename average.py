number = int(input('insert your number: '))
count = 0
sum = 0
while number != -1:
    sum += number
    count += 1
    number = int (input('insert your number: '))

print (sum/count)