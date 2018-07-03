"""
close()
read()
readline(): lee solo una línea
truncate(): vacía el archivo.
write("str"):
seek(int): se mueve/lee la locación al comienzo del archivo

"""
# importa del módulo sys la función argv
from sys import argv

# entrega argumentos a la función argv
script, filename = argv

# Llama a la variable filename que guarda el nombre del archivo
# Para borrarlo a través de confirmación por parte de usuario

print(f"""
We're going to erase {filename}.
If you don't want that, hit CTRL-C (^C).
If you do want that, hit RETURN.
""")
input("?")

# Si el usuario acepta y no sale del programa, abre el archivo
# con el nombre guardado en filename, lo escribe y lo trunca
print("Opening the file..")
target = open(filename, "w")

# REDUNDANTE si se declara "w" Trunca finalmente el archivo abierto
"""
print("Truncating the file. Goodbye!")
target.truncate()
"""

# Pide ingreso de 3 lineas para escribir en el archivo aún abierto
print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# Escribe los input correspondientes a las variables en donde
# Se guardaron sus valores
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# Imprime una linea para dar aviso de que el archivo se cerrará
# Ya que no será siendo ocupado
print("And finally, we close it.")
target.close()
