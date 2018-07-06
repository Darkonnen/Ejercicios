arg = 0 # variable creada con valor 0
print(arg) # muestra en pantalla un string o func()
"# String" # escribe un comentario en una línea de código

""""""    # 3 comillas abren y 3 cierran documentación del código

""" 
Operaciones aritméticas en Python

+ : suma
- : resta
* : multiplicación
** : exponente
/ : división
// : división entera (contrario a módulo)
% : módulo de diferencia en la división


Operadores de asignación

= : asignación de valor
+= : suma var2 a var1
-= : resta var2 a var1
*= : multiplica las variables
/= divide las variables


Operadores de comparación

== : igual a / comparación de variables
!= : distinto a
< : menor que
> : mayor que
<>: comparación var1 no es igual a var2
<= : menor o igual que
>= : mayor o igual que


Operadores lógicos

and : y
or : o
not : no es / no en


Tipos de variable

True, False : Variable boleana
int, float : variables tipo interger (entera) o float (flotante) decimal
#from sys import argv
script, var1, var2..., varn = argv : contiene los argumentos al correr el programa.


Métodos de strings

end = ' ' : le dice al input o print que continuea en la línea
\n : salta una línea en el string
\t : agrega un tab al string
\ : escapa un carácter en el string 
f"str {}" : formatea variables en los {} del string 
str.capitalize() : convierte la primera letra del string en mayúsculas
var1.count("str") : cuenta la cantidad del string en la variable
str.join(seq): retorna un string en donde los elementos de la secuencia han sido unidos por el str separador
max(var) : valor máximo del string
min(var) : valor mínimo del string
var1.replace("str", "STR") : reemplaza un string por otro
var1.strip("char") : remueve los carácteres de adelante y de atrás de un string 
var1.upper() : convierte todo el string en mayúsculas
var1.lower() : convierte todo el string en minúsculas


Métodos de tuplas

cmp() : compara dos tuplas
len() : longitud de la tupla
max() : máximo valor de la tupla
min() : mínimo valor de la tupla
list() : crea una lista con la tupla
count(var): regresa los items con valor igual al argumento
index(var): regresa el índice del valor del argumento
tuple.strip(char) : remueve el carácter designado
sum() : regresa la suma de todos los elementos en la tupla


Métodos de listas

list(var) : convierte una variable en lista
var = [] : crea una lista vacía 
var1.append(arg) : agrega solo un argumento al final de la lista
var1.extend(kwargs) : agrega **argumentos al final de la lista 
list1 + list2 : concatena listas 
var1.insert(index, arg) : inserta un argumento en el índice de la lista
var1.remove(var) : remueve la variable de la lista 
var1.pop(index) : remueve la variable de la lista de acuerdo al índice
var1.count(var) : retorna cuantas variables hay en la lista.
var1.sort((reverse=True): Ordena la lista
sorted(var1) : Devuelve una copia de la lista ordenada, sin afectarla. 
var1 = ','.join(courses) : une los valores de una lista con el carácter designado.
var2 = course_str.split(',') : separa los carácteres de una lista de acuerdo al carácter designado.  
list.split(char) : separa de acuerdo al carácter designado.
var.clear() : vacía una lista.
del list / del list[ : ] : remueve toda la lista o los elementos seleccionados  
var.copy() : retorna una copia de la lista
var1.index(var) : retorna el índice de la variable


Métodos de sets/arreglos # En sets los valores no se repiten!

empty_set = set() # OJO Esto crea un set vacío.
var = set{arg1, arg2}
var.add(arg) : agrega al final del set un argumento
var.update(arg) : actualiza los valores del set
var.discard(arg) : remueve un argumento del set pero sin eliminarlo del set, si no lo encuentra, no envia error.
set.enumerate(arg) : enumera los argumentos y transforma en set
var.remove(arg) : remueve un argumento del set, si no lo encuentra, envia error. 
var.pop() : elimina y guarda el último argumento del set.
var.clear() : elimina todos los argumentos del set.
var.copy() : retorna una copia del set
var1 | var2 : retorna la union de sets.
var1.union(var2) : retorna la union de sets. 
var1 & var2 : interseca ambos sets
var1.intersection(var2) : interseca ambos sets
var1.intersection_update(var2) : actualiza la intersección en ambos sets.
var1 - var2 : resta ambos sets
var1.difference(var2) : resta ambos sets
var1.difference_update(var2) : remueve todos los elementos de otro set al set actual
var1 ^ var2 : diferencia simétrica de sets
var.symmetric_difference(var2) : diferencia simétrica de sets


Métodos de diccionario # En diccionarios los valores no se repiten!

all(dic) : regresa True si todos los argumentos son True en el diccionario
any(dic) : regresa True si al menos un elemento es True en el diccionario
sorted(dic) : jerarquiza y ordena el diccionario
var = {arg1: "arg1", arg2: "arg2"}
var = {} : crea un diccionario vacío
len(dic) : retorna longitud del diccionario
dic.values() : retorna los valores del diccionario
del dic[key] : remueve la clave del diccionario
dic.get(key) : retorna el valor del diccionario
dic.items() : retorna todos los valores/clavedel diccionario
dic.update({key:value}) : actualiza el diccionario con la valor/clave correspondiente
dic.pop(key): remueve y retorna el item con el valor y llave
sorted(dic) : devuelve el diccionario con keys ordenados. 


Estructuras de Control de Flujo

if   : evalua si una función es True o False
elif : Si if es False, evalua la función
else : Si if o elife son False, ejecuta sus argumentos

Ciclos / Bucles

for : itera sobre una secuencia n cantidad de veces
while : itera sobre una secuencia mientras el argumento sea True


Funciones

def function(): define una función
lambda var: function() : crea una función anónima 
pass : salta una parte del ciclo
continue : continua el ciclo
break : sale del ciclo
return : retorna el valor de la función


Clases, Objetos, Funciones y Atributos

class MyClass: 
    args          : define una clase
    
var = MyClass()
print(var(arg))   : Crea un objeto e imprime su argumento

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
                                       
    def myfunc(self):
        print("str" + self.name)
                                        : todas las clases tienen una función
var = Person("John", 36)                 llamada __init_:(), que siempre se ejecuta
print(var.name)                          cuando la clase es iniciada
print(var.age)                            
var.myfunc()                            : llama el método de la clase



Leer archivos:

.close() : 
open(filename, "w", "r", "a"): abre el archivo y escribe, lee o agrega al archivo.
.read(filename) : lee el archivo
.readline() : lee la línea
.truncate() : vacía el archivo
.write("str") :
.seek(index): 


Manejo de errores

try: verifica que el argumento no contenga errores, ejecutando finalmente su contenido. 
except: si Try contiene un error en específico, pasa a except y ejecuta su contenido.
finally: el contenido se ejecuta siempre después de try aún hayan ocurrido errores o no.
raise ERROR: define excepciones de usuario de acuerdo a parámetros ingresados.



Métodos por defecto

abs(var) : regresa el valor absoluto de una variable
any() : regresa True si hay un elemento en la lista
all() : regresa True si todos los elementos son True o si la lista está vacía
ascii() : retorna un string que contiene una representación imprimible de un objeto 
bin(num) :  regresa el valor binario de un integer
bool(arg) : regresa True si el argumento es True y False si no hay argumento o es falso
bytearray() : regresa un objeto matriz de bites mutable
bytes() : regresa un objeto matriz de bites inmutable
callable() : comprueba que el objeto es llamable, sino retorna False
chr() : regresa un carácter unicode asociado a un integer
classmethod(function) : retorna el método de clase de una función
compile() : compila, ver documentación
complex(num1, -num2]) : retorna un numero complejo o convierte un string en numero complejo 
delattr(obj, name) : elimina un atributo de un objeto si este lo permite.
dict(*arg, **kwargs) : crea un diccionario
dir(obj) : retorna una lista de atributos del objeto (por ejemplo en una clase)
divmod(x, y) : regresa cuociente y restante  
enumerate(tuple/list/set) : añade un contador y regresa el objeto enumerado
eval() : evalua la expresión y la corre en python, ver en documentación
exec() : ejecuta un programa, ver en documentación 
filter(function, iterable) : construye un iterador entre una función y una tupla, set o lista 
float(num) : retorna un numero punto flotante de un numero o string
format(num, "b" "f" "b") : retorna una versión formateada a int, float o binary
frozenset(var) : versión inmutable de un iterable tupla, lista, set o diccionario
getattr(object, "name") : retorna el valor del atributo en una clase
globals() / globals()["var"] : retorna el diccionario de la tabla global actual
hasattr(object, "name") : retorna True si un objeto se le ha dado el atributo nominado
hash(object) : retorna el valor hash (secuencia de bytes) si un objeto lo tiene
help(object) : ayuda por default del sistema
hex(var) : convierte un integer a valor hexadecimal
id(object) : regresa la identidad (unique integer) de un objeto en el programa  
input() : lee una línea de input, la convierte en string y la retorna
int() : retorna un integer de un objeto o string
isinstance(object, classinfo) : comprueba si el primer argumento es una instancia o subclase de classinfo
issubclass(objeto, subclase) : comprueba si el primer argumento es una subclase de classinfo
iter(object) : crea un iterador del objeto ('next' continua el iterador)
len() : retorna la longitud de un objeto
list() : crea una lista en python
locals() :  retorna el diccionario de la tabla local actual
map() : aplica una función dada a cada item de un iterable y retorna una lista de los resultados (hay que pasarla a una lista o iterable necesariamente)
max(): retorna el máximo elemento en un iterable 
memoryview() : retorna una memoria de vista de objeto
min() : retorna el elemento mínimo en un iterable
next(iterator) : retorna el elemento siguiente de un iterador (ver iter())
object() : crea un objeto base
oct(int) : toma un int y lo transforma en octal
open(file) : abre un archivo y regresa un archivo objeto "r" leer "w" escribir "x" crear "a" agrega string al final del archivo 
ord(int) : retorna un integer en unicode
pow(x, y) : retorna x a la potencia de y  
print(object) : imprime en pantalla el objeto
property(fget, fset, fdel, doc) @property(): retorna un atributo propiedad (también se puede ocupar como decorador)
range(start, stop, step) : retorna una secuencia inmutable de números entre el comienzo del integer hasta su límite
repr(object) : retorna una representación imprimible del objeto
reversed(seq) : retorna el iterador inverso de la secuencia
round(num, digits) : redondea el punto flotante
set(args) : construye un ser iterable
setattr(object, name, value) : establece el valor del atributo dado de un objeto
slice(start, stop, set) : crea una rebanada de objeto 
sorted(iterable, reverse=True) : retorna una lista ordenada de un iterable, reverse es opcional
staticmethod(function) : retorna una función estática de una función dada
str(object) : convierte en string un objeto
sum(iterable, int) : suma los elementos de un iterable y retorna la suma. También se le puede agregar un valor extra que sume.
super(). : retorna un objeto apoderado que permite referir a su clase padre 
tuple(iterable) : crea una tupla
type(object) : retorna el tipo del objeto
vars(object) : retorna el atributo diccionario del objeto 
zip() : toma iterables, crea iterables y agrega iterables basadas en las iterables pasads, regresándolas como iterador de tuplas. Ver en documentación.
__import__ : función avanzada que es llamada por la declaración import. Ver en documentación.

"""

"""
AssertionError 	Raised when assert statement fails.
AttributeError 	Raised when attribute assignment or reference fails.
EOFError 	Raised when the input() functions hits end-of-file condition.
FloatingPointError 	Raised when a floating point operation fails.
GeneratorExit 	Raise when a generator's close() method is called.
ImportError 	Raised when the imported module is not found.
IndexError 	Raised when index of a sequence is out of range.
KeyError 	Raised when a key is not found in a dictionary.
KeyboardInterrupt 	Raised when the user hits interrupt key (Ctrl+c or delete).
MemoryError 	Raised when an operation runs out of memory.
NameError 	Raised when a variable is not found in local or global scope.
NotImplementedError 	Raised by abstract methods.
OSError 	Raised when system operation causes system related error.
OverflowError 	Raised when result of an arithmetic operation is too large to be represented.
ReferenceError 	Raised when a weak reference proxy is used to access a garbage collected referent.
RuntimeError 	Raised when an error does not fall under any other category.
StopIteration 	Raised by next() function to indicate that there is no further item to be returned by iterator.
SyntaxError 	Raised by parser when syntax error is encountered.
IndentationError 	Raised when there is incorrect indentation.
TabError 	Raised when indentation consists of inconsistent tabs and spaces.
SystemError 	Raised when interpreter detects internal error.
SystemExit 	Raised by sys.exit() function.
TypeError 	Raised when a function or operation is applied to an object of incorrect type.
UnboundLocalError 	Raised when a reference is made to a local variable in a function or method, but no value has been bound to that variable.
UnicodeError 	Raised when a Unicode-related encoding or decoding error occurs.
UnicodeEncodeError 	Raised when a Unicode-related error occurs during encoding.
UnicodeDecodeError 	Raised when a Unicode-related error occurs during decoding.
UnicodeTranslateError 	Raised when a Unicode-related error occurs during translating.
ValueError 	Raised when a function gets argument of correct type but improper value.
ZeroDivisionError 	Raised when second operand of division or modulo operation is zero.




"""
