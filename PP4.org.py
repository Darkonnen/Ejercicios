answ = int(input("Ingresa un número > "))

# ingreso 10

lista = []

for i in range(1, answ+1): # Por cada elemento en el rango

    if answ % i == 0:
        print(f"{i} es divisor")
        lista.append(i)
    else:
        pass

print(lista)
