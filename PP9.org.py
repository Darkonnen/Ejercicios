import random

var = random.randint(1, 9)

while True:

    resp = int(input("Ingresa un número del 1 al 10: > "))

    if resp > var:
        print("Muy arriba")
    elif resp < var:
        print("Muy abajo")

    elif resp == var:

        print("Has acertado!")
        answ = input("Quieres jugar de nuevo? > ")
        answ.lower()
        if answ == "si":
            var = random.randint(1,9)
            continue
        else:
            break