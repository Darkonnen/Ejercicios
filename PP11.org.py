def  primeNumber(num):

    if num == 1:
        print("Not prime")
    elif num == 2:
        print("Prime")

    resp = ''
    for i in range(2, num):
        if num % i == 0:
            resp = "even"
            break
        else:
            resp = "odd"


    print(resp)

answ = int(input("Ingresa un número: > "))
instancePrime = primeNumber(answ)