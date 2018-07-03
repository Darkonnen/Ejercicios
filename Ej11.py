import Red

Red.mostrar_bienvenida()

(nombre, edad, estatura_m, estatura_cm, num_amigos) = Red.obtener_datos()

print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
Red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos)
print("Ya podemos preguntar, recordar y calcular datos. Esperamos que disfrutes con Mi Red")
print("--------------------------------------------------")

opcion = 1
while opcion != 0:
    opcion = Red.opcion_menu()
    if opcion == 1:
        mensaje = Red.obtener_mensaje()
        Red.mostrar_mensaje(nombre, None, mensaje)
    elif opcion == 2:
        mensaje = Red.obtener_mensaje()
        for i in range(num_amigos):
            nombre_amigo = input("Ingresa el nombre de tu amigo o amiga: ")
            Red.mostrar_mensaje(nombre, nombre_amigo, mensaje)
    elif opcion == 3:
        Red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos)
    elif opcion == 4:
        nombre = Red.obtener_nombre()
        edad = Red.obtener_edad()
        (estatura_m, estatura_cm) = Red.obtener_estatura()
        num_amigos = Red.obtener_num_amigos()
        Red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos)
    elif opcion == 0:
        print("Has decidido salir.")

print("Gracias por usar Mi Red. Â¡Hasta pronto!")