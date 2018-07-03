# LEGB rule

# Local, Enclosing, Global, Built-in

import builtins

print(dir(builtins))

x = 'global x'
y = 'global y'

def mymin():
    pass

m = min([5,1,3,2,4])
print(m)

def test(z):
    x = 'local X'
    print(z)

def anTest():
    global y   # ocupa la variable global definida previamente
    y = 'local Y'
    print(y)

test("local z")
anTest()
print(x)
print(y)

def outer(): # Enclosing variable scpoe
    x = 'outer x'

    def inner():
        x = 'inner x'
        print(x)
        """
    def nonl():
        nonlocal x

        x = 'nonlocal x'
        print(x)
        """


    inner()
    #nonl()
    print(x)

outer()
print(x)
