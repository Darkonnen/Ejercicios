# Slice -> strings and lists

lista = [1,2,3,4,5,6,6,2,1,3,21,2]

print(lista[::-1])

sample_url = "000https://www.neuroescuela.cl"
holaMundo = "hola mundo"

print(sample_url)

print(sample_url[8:])

for i in " 0:/.":
    sample_url = sample_url.replace(i, "")

print(sample_url)

a = sample_url.strip('0')
b = holaMundo.strip("h")

print(a)
print(b)
