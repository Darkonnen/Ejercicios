class Duck:

	def quack(self):
		print("Quack, Quack")

	def fly(self):
		print("Flap, Flap")

class Person:

	def quack(self):
		print("I'm Quacking Like a Duck!")


	def fly(self):
		print("I'm Flapping my Arms")

def quack_and_fly(thing):
		thing.quack()
		thing.fly()
"""if is instance(thing, Duck):
		thing.quack()
		thing.fly()
	else:
		print("This has to be a Duck!")"""

d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)