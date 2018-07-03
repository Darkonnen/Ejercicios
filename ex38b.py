"""
# list(var) : convierte una variable en lista
# var = [] : crea una lista vacía
# var1.append(arg) : agrega solo un argumento al final de la lista
# var1.extend(kwargs) : agrega **argumentos al final de la lista
list1 + list2 : concatena listas 
var1.insert(index, arg) : inserta un argumento en el índice de la lista
var1.remove(var) : remueve la variable de la lista 
var1.pop(index) : remueve la variable de la lista de acuerdo al índice
var1.count(var) : retorna cuantas variables hay en la lista  
list.split(char) : separa de acuerdo al carácter designado
var.clear() : vacía una lista.
del list / del list[ : ] : remueve toda la lista o los elementos seleccionados  
var.copy() : retorna una copia de la lista
var1.index(var) : retorna el índice de la variable
"""
listaA = "Palabras Al Azar Separadas Pero En Un String" #8
listaB = ["Ahora", "Si", "Son", "Elementos", "De", "Una", "Lista"] # 7
listaC = []

listaA = list(listaA.split(' '))
print(listaA)
lastB = listaB[-1]    # index
listaA.append(lastB)
lastA = listaA[2:5]
listaC.extend(lastA)
removeB = listaB.pop(3)
print(listaA)
print(listaB)
print(f"\tHe sacado '{removeB}' con índice 3 de la listaB")
print(listaC)
listaC.clear()
print("\n\t\tHe borrado todos los elementos de la listaC > ", listaC)
bIndx = listaB[2] # Un
aIndx = listaA[6] # Son
bIndx.strip()
print(aIndx)
print(bIndx)
listaD = aIndx + bIndx
listaE = []
listaE.append(aIndx)
listaE.append(bIndx)
print(listaD)
print(listaE)
print(type(listaD))
hm = listaB.count("Ahora")
print(hm, "veces")
listaF = listaC.copy()
listaF.insert(0, "valor")
print(listaF)
