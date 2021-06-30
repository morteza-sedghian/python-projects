def hoghoogh(hour, per_hour):
    if hour > 8:
        return 'ziadi kar kardi 0'
    salary = hour * per_hour
    return salary

userH = int (input('Chand saat kar kardi? '))
userPH = int (input('Saati chand migiri? '))

print ('Dast mozdet mishi', hoghoogh(userH,userPH), 'Odlar')