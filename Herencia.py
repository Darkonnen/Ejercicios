class CasaStark: #Super-clase / clase base
    """Personajes de GoT"""
    print("Hijos de Eddard Stark y Lady Catelyn")
    def __init__(self, apellido_stark):
        self.apellido_stark = apellido_stark

class HerederoStark(CasaStark): #Sub-clase / clase derivada
    """Sub-clase que hereda de la clase CasaStark"""
    def nombre(selfself, nombre, apellido_stark):
        print("Mi nombre es ", nombre, " Heredero de la casa ", apellido_stark)
        
#Instanciamos objetos de la clase derivada HerederoStark
robb = HerederoStark("Stark")
sansa = HerederoStark("Stark")
arya = HerederoStark("Stark")
bran = HerederoStark("Stark")
rickon = HerederoStark("Stark")

print(robb.nombre("Robb ", robb.apellido_stark))
print(bran.nombre("Bran ", bran.apellido_stark))
print(arya.nombre("Arya ", arya.apellido_stark))
print(rickon.nombre("rickon ", rickon.apellido_stark))
print(sansa.nombre("Sansa ", sansa.apellido_stark))