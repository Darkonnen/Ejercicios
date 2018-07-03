import builtins

print(dir(builtins))

x = "global X"

m = min([5,1,4,2,3])

print(m)

def test():
	
	y = "local Y"
	x = "local X"
	print(y)
	print(x)

test()
print(x)