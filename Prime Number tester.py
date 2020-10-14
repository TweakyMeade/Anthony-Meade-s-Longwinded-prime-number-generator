starterflag = True
while starterflag:
    # the idea of this loop is that when the user inputs a value it checks to see if its an int,
    # at the present moment its not fully inpemented but i want to have i will add testpasser
    # that will shout at the user trying to be funny and inputing a letter or a float.
    primeNumberBuffer = input("What Number do you want to test?:")
    primeNumbertest = int(primeNumberBuffer)
    if type(primeNumbertest) == int:
        starterflag=False
primeNumberFlag = True
counter = 0 # Initializing Counter
divider = primeNumbertest # setting divider to the inital value of the number requested
while primeNumberFlag:
    #this while loop will find te the results of the Number divided
    primeResult=primeNumbertest % divider
    if primeResult == 0:
        counter +=1
    divider -= 1
    if divider == 1:
        primeNumberFlag = False
if counter <= 2: # inte
    print(primeNumbertest, "is a prime number")
else:
    print(primeNumbertest, "is not a prime number")
