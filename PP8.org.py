import random
while True:
    answ = str(input("Jugar? (si/no)> "))
    answ = answ.lower()

    if answ == "si":
        rps = str(input("Piedra, Papel o Tijera? > "))
        rps = rps.lower()
        rpsList = ["piedra", "papel", "tijera"]
        champ = random.choice(rpsList)
        print("Yo elijo {}".format(champ))
        if rps == "piedra" and champ == "piedra" or rps == "tijera" and champ == "tijera" or rps == "papel" and champ == "papel":
            print("Hemos empatado!")

        elif rps == "papel" and champ == "piedra" or rps == "piedra" and champ == "tijera" or rps == "tijera" and champ == "papel":
            print("Has ganado. Felicitaciones!")

        elif rps == "piedra" and champ == "papel" or rps == "tijera" and champ == "piedra" or rps == "papel" and champ == "tijera":
            print("Te he ganado!")

        else:
            print("Debes contestar una de las opciones señaladas")

    elif answ == "no":
        print("Goodbye")
        exit(1)

    else:
        print("Responde 'si' o 'no' > ")
