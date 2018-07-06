answ = str(input("Escribe algo > "))
wsna = reversed(answ)
reversedString = ''.join(wsna)

if answ == reversedString:
    print("Son iguales")
else:
    print("son distintas")
