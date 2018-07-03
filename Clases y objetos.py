""" 
class MiClaseEjemplo:
    #clases, objetos y métodos
    entero = 4321
    def mensaje(self, mensaje):
        print(mensaje)
    #instanciar objeto de la clase
x = MiClaseEjemplo()
y = MiClaseEjemplo()
print(x.entero)
print(y.mensaje("Hola POO"))

"""

class MiPerro():
    def __init__(self, raza):
        self.raza = raza

    def ladrar(self, ladrido, raza):
        print(ladrido, raza)

    def juego(self, jugar):
        print(jugar)

    def proteger(self, cuidar):
        print(cuidar)

baltazar = MiPerro("Dálmata")
perrales = MiPerro("Daschund")

#Accedemos a su atributo
print(baltazar.raza)
print(perrales.raza)

#Accedemos a los métodos

baltazar.ladrar("guaf me llamo baltazar y soy un ", baltazar.raza)
perrales.ladrar("guaf me llamo Tufo y soy un", perrales.raza)