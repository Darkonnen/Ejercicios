x = "Hello, world!"
y = ["Uno", "Dos", "Tres"]
z = list((1, 2, 3))
w = list(("Uno", "Dos", "Tres"))
t = list(("Math", "Art", "CompSci"))
tupla = tuple(("T1", "T2", "T3"))
k = {"Soya", "Vegetales", "Café"}
l = set(("Jugo", "Arroz", "Té"))




print(x.replace("H","J"))
print(y[2])
print(z)
print(w.remove("Dos"))

y.append("Cuatro")
z.clear()
a = y.copy()
b = y.count("Uno")
y.extend(["Cinco", "Seis"])
w.insert(1, "Universe")
w.pop(0)
t.remove("Art")
t.sort()
l.remove("Té")
l.add("Gato")

print(y)
print(y)
print(z)
print(a)
print(b)
print(y)
print(y.index("Tres"))
print(w)
print(t)
print(tupla)
print(k)
print(l)


"""

# Tuplas
var = tuple(())
len("str")

# Listas
var = list(())
.append()
.clear()
.copy()
.count("str")
.extend("str")
.index("str")
.insert(var, "str")
.len(list)
.pop(int)
.remove()
.reverse()
.sort()

# Sets
var = set(())
.add("str")
.remove("str")
.len()

# Diccionario

name = dict(var1 = "str", var2 = "str2")
del(name["str"])
len()

"""

def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(2)

name = "Aedel"

def funcion(arg):
	print(arg + name + ", Bienvenido!")

funcion("Eres ")

def retornar(v):
	return print(v*5)

retornar(7)

miFuncion = lambda u: u*2

print(miFuncion(8))


funcDos = lambda k: (k*3)/4

print(funcDos(5))

funcTres = lambda j,m: j*m

print(funcTres(6,3))

def miFunc(n):
	return lambda i: i*n

doubler = miFunc(2)
tripler = miFunc(3)

val = 11

print("Doubled: " + str(doubler(val)) + ". Tripled: " + str(tripler(val)) + ".")

class MyClass:
	x = 5

p1 = MyClass()

print(p1.x)

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def myfunc(self):
		print("Hello my name is: " + self.name)

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

p1.myfunc()

# del p1.age
# del p1