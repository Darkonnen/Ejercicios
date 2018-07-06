# Write a program (function!) that takes a list and returns
# a new list that contains all the elements of the
# first list minus all the duplicates.

liOne = [1,1,1,2,3,4,5,5,5,6,7,7,7,8,9,10,10,10,11,12,12,13,14,14,14,15]

# Debiese tener 6,7,8,9,10,11,12,13,14,15

def FuncToSet(object):
    object = set(object)
    return object

def FuncToList(object):
    object = list(object)
    return object

instanciaLista = FuncToSet(liOne)
instanciaSet = FuncToList(instanciaLista)

print(instanciaLista)
print(instanciaSet)

