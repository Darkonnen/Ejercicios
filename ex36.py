# IF siempre debe tener un else. Aunque no tenga sentido
# Se debe agregar una función die

# page 147
import sys
from sys import argv
import random

script, name = argv

def start():
    print("Aquí comienza la historia")
    print("Estás en el umbral de una caverna. (salir / entrar)")
    ans = input()
    ans = ans.lower()
    if ans == "salir":
        fuera()
    elif ans == "entrar":
        dentro()
    else:
        start()

def win():
    print("Has ganado!")

def gameover():
    print("Has perdido!")

def fuera():
    print("Estás fuera de la caverna")
    print("Te has perdido la aventura")


def dentro():
    print("Estás dentro de la caverna")
    print("Encuentras un acertijo para resolver")

    x = random.randint(1, 5)
    choices = ["+", "-", "*", "/"]
    y = random.randint(6, 10)
    elec = random.choice(choices)
    print(x, elec, y)
    a = choices.index(elec)
    print("index", a)

    if a == 0:
        resp = x + y
    elif a == 1:
        resp = x - y
    elif a == 2:
        resp = x * y
    else:
        resp = x / y

    print(f"Cuánto es {x} {elec} {y}")
    print("Resuélvelo o morirás")
    answer = int(input("Respuesta? > "))

    if answer == resp:
        win()
    else:
        gameover()



print("Hola, aventurero.")

def aventura():
    print("Quieres comenzar la aventura? (Si/No) > ", end = ' ')
    a = input()
    a = a.lower()
    if a == "si":
        start()

    elif a == "no":
        sys.exit()

    else:
        print("Debes ingresar una opción")
        aventura()

print(f"Hola {name}")
aventura()
