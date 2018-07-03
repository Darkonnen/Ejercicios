# define una clase llamada Parent
class Parent(object):

    def implicit(self):
        print("PARENT implicit()")

    def override(self):
        print("PARENT override()")

    def altered(self):
        print("PARENT altered()")

# define una clase llamada Child que hereda las características de la clase Parent
class Child(Parent):

# define una función propia, distinta a la heredada
    def override(self):
        print("CHILD override()")

# define una función similar a la de la clase Parent
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")

        # función super(class, self).function permite acceder a su propia caracteristica, sin la herencia
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")


dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()

