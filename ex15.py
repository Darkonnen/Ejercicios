# Importa un módulo para separar argumentos
# en variables al ejecutar el programa

from sys import argv

# declara los argumentos que toma la variable argv
script, filename = argv

# define el argumento de txt como la función open(nombre_de_archivo)
txt = open(filename)

# Escribe en pantalla un string que muestra el archivo abierto
# El archivo fue declarado al ejecutar en el terminal
print(f"Here's your file {filename}:")

# lee la variable text, la cual abre el archivo filename
print(txt.read())

# muestra en pantalla un string que pide ingresar un nuevo nombre de archivo
print("Type the filename again:")

# esta línea es el input del nombre del archivo
file_again = input("> ")

# Abre el archivo, guardado en la variable file_again
txt_again = open(file_again)

# Lee y abre el segundo archivo.
print(txt_again.read())
