estudiante = {"nombre": "Aedel", "edad": 31, "profesión": "Neurocientífico"}

print(estudiante["nombre"])
print(estudiante["edad"])
print(estudiante.get("nombre"))
print(estudiante.get("herramienta", "No encontrado"))

estudiante["teléfono"] = "+56987175530"
print(estudiante.get("teléfono"))
estudiante["teléfono"] = "87175530"
print(estudiante.get("teléfono"))
estudiante.update({"nombre": "Adel", "deporte": "JiuJitsu"})
print(estudiante)
del estudiante["deporte"]
remover = estudiante.pop("edad")
print(f"removí el valor edad con key {remover}")
print(estudiante)
print(len(estudiante))
print(estudiante.keys()) # devuelve las llaves del diccionario
print(estudiante.values()) # devuelve los valores del diccionario
print(estudiante.items()) # devuelve los elementos del diccionario

for key in estudiante:
    print(key)

for key, values in estudiante.items():
    print(key, values)