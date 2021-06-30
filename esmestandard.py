def gereftaneasami(asami):
    for i in range(0, 10):
        asami.append(input())
    return asami

def kuchikkon(darham):
    for i in range(0,10):
        darham[i] = (darham[i]).lower()
    return darham

def avalbozorg(avalghati):
    for i in range(0, 10):
        avalghati[i] = (avalghati[i][:1]).upper() + avalghati[i][1:]
    return avalghati

def namayesh(nahaii):
    for i in range(0, 10):
        print(nahaii[i])

namha = []
gereftaneasami(namha)
namayesh(avalbozorg(kuchikkon(namha)))