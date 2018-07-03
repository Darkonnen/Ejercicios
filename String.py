cadena = input ("Digite una cadena de texto: ")

print("\n El número de carácteres de la cadena es: ", len(cadena))

if cadena.isalpha():
    print("\n La cadena es alfabética")

if cadena.isdigit():
    print("\n La cadena es numérica")

print("\n En mayúsculas: ", cadena.isupper())

print("\n En minúsculas: ", cadena.islower())

print("\n Invierte: ", cadena.swapcase())

print("\n Reemplaza a por x: ", cadena.replace("a", "x"))

print("\n Posición del carácter: ", cadena.find("a"))

print("\n Posición del carácter: ", cadena.rfind("a"))

print("\n Lista de sub-cadenas: ", cadena.split("a"))