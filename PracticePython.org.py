from datetime import datetime

nombreInfo = str(input("nombre? > "))
edadInfo = int(input("edad? > "))
nVeces = int(input("Cuantos mensajes quieres? > "))

while nVeces <= 0:
    if nVeces <= 0:
        print("Debes escribir un número positivo mayor a cero")
        nVeces = int(input("Cuantos mensajes quieres? > "))
    else:
        break
# Entrada 30
anoCien = 100 - edadInfo # resta la edad
anoActual = datetime.now().year # año actual
anoSuma = anoCien + anoActual

print(f"Estimado {nombreInfo}, estamos en el {anoActual} "
      f"y en el {anoSuma} tendrás 100 años!\n" * nVeces)