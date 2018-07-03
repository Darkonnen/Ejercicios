import sys

print("\nEste es el juego del Demiurgo")
print("\t No tienes por qué jugarlo\n a menos que quieras conocer...\nla...\nverdad...")
a = input("¿Te aventuras en la caverna de los Dioses?(Si / No)> ")
a = a.lower()

while a != "si":
    if a == "no":
        print("Adiós")
        sys.exit()
    else:
        a = input("Ingresa Si o No > \n")
        a = a.lower()

print(f"Tu respuesta fue {a}")
print("Ahora comienza la aventura...")
print("Entras en una caverna y ves al Demiurgo que te observa\ncon sus ojos vacíos")
print("¿Qué haces? "
        "1. Le hablas. "
        "2. Escapas. > ", end = ' ')
b = input()

if b == 1:
    print("Te responde en un idioma ancestral que reconoces, es el idioma de tus sueños")
    print("Caes en un profundo sueño y mueres lentamente cayendo en el abusmo de la locura en el reino onírico")

elif b == 2:
    print("El Demiurgo te atrapa por la espalda y te tortura durante mil años por cobarde,")

else:
    print("Te quedas quieto. Meditas. Te das cuenta de que tu eras el Demiurgo")
    print("Felicitaciones.")
    print("Quieres jugar otra vez? (Si/No)> ")
    a = input()
