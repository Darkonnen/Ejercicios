# Diccionarios

instrumentos = {"Guitarra":"Cuerdas", "Violín": "Cuerdas", "Piano":"Teclas", "Batería":"Tambores"}

puedesTocar= {"Cuerdas" : "Rock", "Teclas": "Clásica", "Tambores": "Metal"}

noMusic = {"Cuerdas" in instrumentos}

nums = {1,2,3,4}
letters = [a,b,c,d]

# verifica si hay algún elemento y/o el elemento es True y lo imprime
print(any(puedesTocar))
# verifica si todos los elementos son True o si no tiene elementos y lo imprime
print(all(noMusic))
# retorna
a = puedesTocar.get("Teclas")
b = instrumentos.get("Piano")
noMusic.clear()
list(noMusic)
print(len(noMusic))

print(puedesTocar.items())
c = instrumentos.pop("Violín")
d = puedesTocar.pop("Tambores")

e = {c:d}
print(e)
e.update({"instrumentos": "elementos"})
print(e)
print(sorted(instrumentos))
print(instrumentos.values())
print(puedesTocar.get("Cuerdas"))
print(puedesTocar.items())

for instrum, elemnt in list(instrumentos.items()):
    print(f"El {instrum} tiene {elemnt}")