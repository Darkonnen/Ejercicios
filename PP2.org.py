answ = True

while answ == True:

    a = str(input("Quieres comenzar una partida? (si/no> "))
    a = a.lower()

    if a == "si":
        num = int(input("Ingresa un número > "))
        num2 = int(input("Ingresa otro número > "))

        if num % 2 == 0:
            print(f"El número {num} es par!")
            if num % 4 == 0:
                print(f"Has elegido el número {num}, el cual es múltiplo de 4!")
        else:
            print(f"El número {num} es primo!")

        if num % num2 == 0:
            print(f"Felicitaciones, escogiste {num} y {num2}, dos números que, divididos, dan resto 0!")

        else:
            print(f"Los números ingresados {num} y {num2} no dan división cero.")

    else:
        print("Adiós!")
        exit(1)



