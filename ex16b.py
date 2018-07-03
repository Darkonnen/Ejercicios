from sys import argv

script, filename = argv

print(f"vamos a formatear el archivo {filename}")

objet = open(filename, "w")
objet.truncate()

line1 = input("ingresa un string")
line2 = input("ingresa un string")
line3 = input("ingresa un string")

objet = open(filename, "w")

objet.write(line1)
objet.write("\n")
objet.write(line2)
objet.write("\n")
objet.write(line3)
objet.write("\n")


print("listo")
objet.close()