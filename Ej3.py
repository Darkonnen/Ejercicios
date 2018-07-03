llueve = True
temperatura = int(input("Ingresa temperatura: "))
if temperatura < 18 and llueve == True:
    print("Llevaré paraguas y abrigo")
elif temperatura <18 and llueve != True:
    print("Solo llevaré abrugo")
else:
    print("No llevaré paraguas ni abrigo")

