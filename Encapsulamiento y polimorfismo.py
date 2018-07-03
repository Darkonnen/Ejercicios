"""

class Aeronave:
    def viajar(self):
        print("Yo viajo por los aires")

class Automovil:
    def viajar(self):
        print("Yo viajo por los caminos")

zeppelin = Aeronave()
coche = Automovil()

zeppelin.viajar()
coche.viajar()

"""

class Ejemplo:
    def __init__(self):
        self.__oculto = "Me encuentro oculto en la clase"

    def publico(self):
        return "soy un método público. A la vista de todos!"

    def __privado(self):
        print ("Soy un método privado. Para ti no existo!")

    def get_oculto(self):
        return self.__oculto

    def set_oculto(self):
        self.__oculto = self.__privado
#Instanciamos un objeto de la clase ejemplo

objeto = Ejemplo()

#Intentamos acceder al método público

#print(objeto.publico())

#Intentamos acceder al método privado

#print(objeto.__privado())

# name mangling

#print(objeto._Ejemplo__privado())

# obtener get_oculto

#print(objeto.get_oculto())
objeto.set_oculto()