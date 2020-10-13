priCand = 1
primeFlag = True
while primeFlag:
    counter = 0
    primeFlagTwo = True
    priCand += 1
    dvd = priCand
    while primeFlagTwo:
        if dvd > 0:
            priPro = priCand % dvd
        if priPro == 0:
            counter += 1
        dvd -= 1
        if dvd == 0:
            primeFlagTwo = False
    if counter <= 2:
        print(priCand, "\n")
    if priCand == 0:
        primeFlag = False
