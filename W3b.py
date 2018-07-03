#j = open("demo.txt", "x")
j = open("demo.txt", "r")
print(j.readlines())

j = open("demo.txt", "a")

j.write("Hello World! ")

j = open("demo.txt", "r")
sta = j.read()
print(len(sta))
for line in j:
	print(line)
j.close()

