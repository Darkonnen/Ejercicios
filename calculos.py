def suma():
	"""Suma de dos números ingresados"""
	a = int(input("Ingrese un número entero: "))
	b = int(input("Ingrese un número entero: "))
	print(a + b)

def resta():
	"""Suma de dos números ingresados"""
	a = int(input("Ingrese un número entero: "))
	b = int(input("Ingrese un número entero: "))
	print(a - b)

def multiplicacion():
	"""Suma de dos números ingresados"""
	a = int(input("Ingrese un número entero: "))
	b = int(input("Ingrese un número entero: "))
	print(a * b)

def division():
	"""Suma de dos números ingresados"""
	a = int(input("Ingrese un número entero: "))
	b = int(input("Ingrese un número entero: "))
	print(a / b)

def fib(n):
	"""fibonacci"""
	x = 0
	y = 1
	while x < n:
		print(x)
		x = y
		y = x + y
	print()
