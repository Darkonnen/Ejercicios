"""

def LetterCapitalize(str):

    for i in str:
        str = str.split(' ')
        a = str[0]
        b = str[1]
    return str

string = "hola mundo"
string = LetterCapitalize(string)

print(string)


frase = "hola mundo"
frase = frase.split(' ')
print(frase)
string = ' '

for i in frase:
    string = string + ' '+ i.capitalize()
    string = string.strip(' ')
print(string)


"""
def LetterCapitalize():
    frase = "hola mundo como estas"
    frase = frase.split(' ')
    string = ' '

    for i in frase:
        string = string + ' ' + i.capitalize()
        string = string.lstrip(' ')
    return (string)

instanciaMayus = LetterCapitalize()
print(instanciaMayus)
print(len(instanciaMayus))


# Segundo ejercicio

def SegundoEjercicio():
    frase2 = "una taza de café"
    frase2 = frase2.split()
    print(frase2)
    stringVacio = ''

    for palabra in frase2:
        stringVacio = stringVacio + ' ' + palabra.capitalize()
        stringvacio = stringVacio.strip(' ')
    return stringVacio

segundaInstancia = SegundoEjercicio()
print(segundaInstancia)




def SimpleSymbols(str):
    flag = True
    if len(str) < 3:
        return "false"
    for x in range(1,len(str)):
        if str[x].isalpha() and (str[x-1] != "+" or str[x+1] != "+"):
            flag = False
    if flag:
        return "true"
    else:
        return "false"


instanceSymbols = SimpleSymbols("++d+===+c++==a")
print(instanceSymbols)

def CheckNums(num1, num2):
    if num2 > num1:
        return "true"
    elif num1 > num2:
        return "false"
    else:
        return -1

instancNums = CheckNums(3,5)
print(instancNums)

strin = "hola mundo"
a = len(strin.split())
print(a)

cd = "aeea"
# bb = ''.join(reversed(cd)) -> Mejor método. Avanzado.
bb = reversed(cd)
bb = str(cd)

if cd == bb:
    print("True")
else:
    print("False")

print(cd)
print(bb)


















