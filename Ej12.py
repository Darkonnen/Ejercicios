lectura = open("abc1.txt", "r")
leer = lectura.read()
print(leer)
lectura.close()

escritura = open("efg2.txt", "w")
escribir = escritura.write("Ya soy el mejor")
print(escribir)
lectura.close()


lectura = open("efg2.txt", "r")
leer = lectura.read()
print(leer)
lectura.close()