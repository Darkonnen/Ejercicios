"""
def LongestWord(sen):
  longest = ""
  longestCount = 0
  for x in sen.split():
      tempCount = 0
      for y in x:
         if y.isalpha():
            tempCount += 1
      if tempCount > longestCount:
          longestCount = tempCount
          longest = x
  return longest

inst = LongestWord("world hello")
print(inst)

"""
"""
def LetterChanges(str):
  result = ""

  for x in str:
    if x == "z":
      newChar = "a"
    elif x == "Z":
      newChar = "A"
    elif x.isalpha():
      newChar = chr(ord(x) + 1)
    else:
      newChar = x

    if newChar in "aeiou":
      newChar = newChar.upper()
    result = result + newChar

  return result

letchng = LetterChanges("Aedel Darko")
print(letchng)

"""

def SimpleAddingSum(num):
    cont = 0

    for i in range(1, num+1):
        cont = cont + i
    return cont

suma = SimpleAddingSum(3)
print(suma)

# Segundo ejercicio

num2 = 5
sum2 = 0

for i in range(1, num2+1):
    sum2 = sum2 + i

print(sum2)

# Tercer ejercicio

num3 = 6
sum3 = 0

for i in range(1, num3+1):
    sum3 = sum3 + i

print(sum3)

# Cuarto ejercicio

sum4 = 0
num4 = 7

for i in range(1, num4+1):
    sum4 = sum4 + i

print(sum4)

# Quinto ejercicio

num5 = 8
sum5 = 0

for n in range(1, 9):
    sum5 = sum5 + n

print(sum5)

# Sexto ejercicio

num9 = 9

def Suma6(num9):
    sum6 = 0

    for n in range(1, num9+1):
        sum6 = sum6 + n
    return sum6

sumaSeis = Suma6(num9)
print(sumaSeis)


# Séptimo ejercicio

num7 = 10
suma7 = 0

def SepttimaSuma(object):
    global suma7, num7
    for j in range(1, num7+1):
        suma7 = suma7 + j

    return suma7

varSiete = SepttimaSuma(num7)
print(varSiete)

# Octavo ejercicio

numero8 = 11
suma8 = 0

def OctavaSuma(object):
    global numero8, suma8
    for g in range(1, numero8+1):
        suma8 = suma8 + g
    return suma8

sumaOcho = OctavaSuma(numero8)
print(sumaOcho)


# Noveno ejercicio!!! Ya voy entendiendo más sobre funciones e instancias

def NovenaSuma(object):

    novenoNum = 12
    sumaNueve = 0

    for m in range(1, novenoNum+1):
        sumaNueve = sumaNueve + m

    return sumaNueve

instanNueve = NovenaSuma(12)
print(instanNueve)


# Décimo ejercicio

numeroDiez = 13
sumaDiez = 0

def SumaDiez(object):
    global numeroDiez, sumaDiez
    for k in range(1, numeroDiez+1):
        sumaDiez = sumaDiez + k
    return sumaDiez

calcularSuma = SumaDiez(numeroDiez)
print(calcularSuma)